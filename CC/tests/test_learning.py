import unittest
from unittest.mock import MagicMock, patch

from app.learning import (
    LEARNING_CATEGORIES,
    STUDY_MODULES,
    get_categories_for_profile,
    get_modules_for_profile,
    render_learning_page,
)
from app.roadmap import ROADMAPS


class LearningCategoryTests(unittest.TestCase):
    def test_initial_catalog_has_four_unique_categories(self):
        category_ids = [category.id for category in LEARNING_CATEGORIES]

        self.assertEqual(len(category_ids), 4)
        self.assertEqual(len(category_ids), len(set(category_ids)))

    def test_categories_are_aligned_with_quiz_profiles(self):
        categories_by_profile = {
            profile: {category.id for category in get_categories_for_profile(profile)}
            for profile in ("programming", "tech", "beginner")
        }

        self.assertEqual(
            categories_by_profile["programming"],
            {"fundamentos-computacao", "programacao"},
        )
        self.assertEqual(
            categories_by_profile["tech"],
            {
                "fundamentos-computacao",
                "tecnologia-sistemas",
                "ferramentas-produtividade",
            },
        )
        self.assertEqual(
            categories_by_profile["beginner"],
            {"fundamentos-computacao", "programacao", "tecnologia-sistemas"},
        )

    def test_unknown_profile_uses_beginner_categories(self):
        self.assertEqual(
            get_categories_for_profile("unknown"),
            get_categories_for_profile("beginner"),
        )

    def test_initial_modules_have_valid_categories_links_and_study_details(self):
        category_ids = {category.id for category in LEARNING_CATEGORIES}
        categories_by_id = {category.id: category for category in LEARNING_CATEGORIES}
        module_ids = [module.id for module in STUDY_MODULES]
        normalized_urls = [
            module.url.strip().rstrip("/").casefold()
            for module in STUDY_MODULES
        ]

        self.assertGreaterEqual(len(STUDY_MODULES), 10)
        self.assertEqual(len(module_ids), len(set(module_ids)))
        self.assertEqual(
            len(normalized_urls),
            len(set(normalized_urls)),
            "Study modules should not repeat the same external material URL.",
        )
        for module in STUDY_MODULES:
            with self.subTest(module=module.id):
                self.assertIn(module.category_id, category_ids)
                self.assertTrue(module.url.startswith("https://"))
                self.assertGreater(module.study_minutes, 0)
                self.assertTrue(module.activity)
                self.assertTrue(module.roadmap_topics)
                roadmap_topics = {
                    topic
                    for profile in categories_by_id[module.category_id].profiles
                    for topic in ROADMAPS[profile]
                }
                self.assertTrue(set(module.roadmap_topics) & roadmap_topics)

    def test_every_roadmap_topic_has_a_module_for_its_profile(self):
        categories_by_id = {category.id: category for category in LEARNING_CATEGORIES}

        for profile, topics in ROADMAPS.items():
            profile_category_ids = {
                category.id for category in get_categories_for_profile(profile)
            }
            for topic in topics:
                with self.subTest(profile=profile, topic=topic):
                    matching_modules = [
                        module
                        for module in STUDY_MODULES
                        if module.category_id in profile_category_ids
                        and topic in module.roadmap_topics
                    ]
                    self.assertTrue(
                        matching_modules,
                        f"No study module for {profile!r} roadmap topic {topic!r}",
                    )
                    self.assertTrue(
                        all(
                            profile in categories_by_id[module.category_id].profiles
                            for module in matching_modules
                        )
                    )

    def test_modules_can_be_filtered_by_profile_category_and_level(self):
        programming_modules = get_modules_for_profile("programming")

        self.assertTrue(programming_modules)
        self.assertTrue(
            all(
                module.category_id in {"fundamentos-computacao", "programacao"}
                for module in programming_modules
            )
        )
        self.assertEqual(
            get_modules_for_profile(
                "programming",
                category_id="programacao",
                level="Intermediário",
            )[0].id,
            "python-controle-fluxo",
        )
        self.assertEqual(
            get_modules_for_profile("programming", category_id="tecnologia-sistemas"),
            (),
        )

    def test_modules_can_be_filtered_by_roadmap_topic(self):
        modules = get_modules_for_profile(
            "beginner",
            roadmap_topic="Estudo guiado com ritmo leve",
        )

        self.assertTrue(modules)
        self.assertTrue(
            all(
                "Estudo guiado com ritmo leve" in module.roadmap_topics
                for module in modules
            )
        )

    def test_learning_page_shows_all_categories_without_quiz_profile(self):
        with (
            patch("app.learning.st.markdown") as markdown,
            patch("app.learning.st.info") as info,
            patch("app.learning.st.columns", return_value=[MagicMock(), MagicMock(), MagicMock()]),
            patch("app.learning.st.selectbox", side_effect=lambda label, options, **kwargs: options[0]),
            patch("app.learning.st.container", return_value=MagicMock()),
            patch("app.learning.st.link_button") as link_button,
        ):
            render_learning_page()

        self.assertEqual(link_button.call_count, len(STUDY_MODULES))
        self.assertTrue(
            any("Complete o quiz" in call.args[0] for call in markdown.call_args_list)
        )
        info.assert_called_once()

    def test_learning_page_filters_categories_by_profile(self):
        with (
            patch("app.learning.st.markdown"),
            patch("app.learning.st.info"),
            patch("app.learning.st.columns", return_value=[MagicMock(), MagicMock(), MagicMock()]),
            patch("app.learning.st.selectbox", side_effect=lambda label, options, **kwargs: options[0]),
            patch("app.learning.st.container", return_value=MagicMock()),
            patch("app.learning.st.link_button") as link_button,
        ):
            render_learning_page("tech")

        self.assertEqual(
            link_button.call_count,
            len(get_modules_for_profile("tech")),
        )

    def test_learning_page_applies_category_and_level_filters(self):
        def select_filter(label, options, **kwargs):
            if label == "Categoria":
                return "Programação"
            if label == "Nível":
                return "Intermediário"
            return options[0]

        with (
            patch("app.learning.st.markdown"),
            patch("app.learning.st.info"),
            patch("app.learning.st.columns", return_value=[MagicMock(), MagicMock(), MagicMock()]),
            patch("app.learning.st.selectbox", side_effect=select_filter),
            patch("app.learning.st.container", return_value=MagicMock()),
            patch("app.learning.st.link_button") as link_button,
        ):
            render_learning_page("programming")

        self.assertEqual(link_button.call_count, 1)
        self.assertEqual(
            link_button.call_args.args[1],
            "https://docs.python.org/3/tutorial/controlflow.html",
        )

    def test_learning_page_filters_modules_by_roadmap_topic(self):
        def select_filter(label, options, **kwargs):
            if label == "Etapa do roadmap":
                return "Estudo guiado com ritmo leve"
            return options[0]

        with (
            patch("app.learning.st.markdown"),
            patch("app.learning.st.info"),
            patch("app.learning.st.columns", return_value=[MagicMock(), MagicMock(), MagicMock()]),
            patch("app.learning.st.selectbox", side_effect=select_filter) as selectbox,
            patch("app.learning.st.container", return_value=MagicMock()),
            patch("app.learning.st.link_button") as link_button,
        ):
            render_learning_page("beginner")

        self.assertEqual(link_button.call_count, 1)
        self.assertEqual(
            link_button.call_args.args[1],
            "https://blockly.games/?lang=pt-br",
        )
        topic_filter = next(
            call for call in selectbox.call_args_list if call.args[0] == "Etapa do roadmap"
        )
        self.assertIn("Estudo guiado com ritmo leve", topic_filter.args[1])


if __name__ == "__main__":
    unittest.main()