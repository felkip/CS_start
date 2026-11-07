import re
import unittest
from pathlib import Path
from typing import cast
from unittest import mock

from app.ui import (
    ICON_NAMES,
    get_icon_svg,
    render_button_group,
    render_empty_state,
    render_feature_card,
    render_icon_button,
    render_icon_text_input,
    render_profile_badge,
    render_quiz_progress,
    render_roadmap_item,
    render_stat_card,
)


class IconTests(unittest.TestCase):
    @staticmethod
    def contrast_ratio(first: str, second: str) -> float:
        def luminance(color: str) -> float:
            channels = [int(color[index : index + 2], 16) / 255 for index in (1, 3, 5)]
            linear = [
                channel / 12.92
                if channel <= 0.04045
                else ((channel + 0.055) / 1.055) ** 2.4
                for channel in channels
            ]
            return (
                0.2126 * linear[0]
                + 0.7152 * linear[1]
                + 0.0722 * linear[2]
            )

        lighter, darker = sorted(
            (luminance(first), luminance(second)),
            reverse=True,
        )
        return (lighter + 0.05) / (darker + 0.05)

    def test_primary_brand_color_meets_aa_for_white_text(self):
        project_root = Path(__file__).parent.parent
        token_sources = (
            project_root / "static" / "style.css",
            project_root / "app" / "theme.py",
        )

        for path in token_sources:
            with self.subTest(path=path.name):
                source = path.read_text(encoding="utf-8")
                match = re.search(
                    r"--brand-primary:\s*(#[0-9a-fA-F]{6})",
                    source,
                )
                if match is None:
                    self.fail("Missing --brand-primary design token")
                self.assertGreaterEqual(
                    self.contrast_ratio("#ffffff", match.group(1)),
                    4.5,
                )

    def test_brand_accents_meet_aa_for_white_background_text(self):
        for color in ("#2563eb", "#6d28d9"):
            with self.subTest(color=color):
                self.assertGreaterEqual(
                    self.contrast_ratio("#ffffff", color),
                    4.5,
                )

    def test_brand_surfaces_do_not_mix_palette_gradients(self):
        project_root = Path(__file__).parent.parent
        style_sources = (
            project_root / "static" / "style.css",
            project_root / "app" / "theme.py",
            project_root / "app" / "ui.py",
            project_root / "app" / "quiz.py",
        )
        for path in style_sources:
            with self.subTest(path=path.name):
                for line in path.read_text(encoding="utf-8").splitlines():
                    if "linear-gradient" not in line:
                        continue
                    brand_colors = re.findall(
                        r"var\(--brand-(?:primary|secondary|accent)\)",
                        line,
                    )
                    self.assertLessEqual(len(brand_colors), 1, line)

    def test_link_and_download_buttons_have_legible_brand_surfaces(self):
        style = (
            Path(__file__).parent.parent / "static" / "style.css"
        ).read_text(encoding="utf-8")
        for selector in (
            '[data-testid="stLinkButton"] a',
            ".stDownloadButton > button",
        ):
            with self.subTest(selector=selector):
                self.assertIn(selector, style)
        self.assertIn("background: var(--brand-primary) !important;", style)
        self.assertIn("color: var(--text-on-brand) !important;", style)
        self.assertIn("background: var(--brand-primary-hover) !important;", style)

    def test_dark_sidebar_secondary_buttons_have_visible_surface_and_focus(self):
        theme = (
            Path(__file__).parent.parent / "app" / "theme.py"
        ).read_text(encoding="utf-8")
        for selector in (
            '[class*="st-key-sidebar-nav-"] [data-testid="stButton"] > button[kind="secondary"]',
            '[class*="st-key-sidebar-logout"] [data-testid="stButton"] > button',
        ):
            with self.subTest(selector=selector):
                self.assertIn(selector, theme)

        self.assertIn("background: var(--bg-subtle) !important;", theme)
        self.assertIn("color: var(--text-primary) !important;", theme)
        self.assertIn("outline: 3px solid var(--focus-ring) !important;", theme)
        self.assertGreaterEqual(
            self.contrast_ratio("#f8fafc", "#1e293b"),
            4.5,
        )

    def test_sidebar_expand_button_has_visible_icon_in_both_themes(self):
        style = (
            Path(__file__).parent.parent / "static" / "style.css"
        ).read_text(encoding="utf-8")
        for selector in (
            '[data-testid="stExpandSidebarButton"]',
            '[data-testid="stExpandSidebarButton"] [data-testid="stIconMaterial"]',
        ):
            with self.subTest(selector=selector):
                self.assertIn(selector, style)

        self.assertIn("color: var(--text-secondary) !important;", style)
        self.assertIn("opacity: 1 !important;", style)
        self.assertIn("border: 1px solid var(--border) !important;", style)
        self.assertIn("[data-testid=\"stExpandSidebarButton\"]:focus-visible", style)
        self.assertGreaterEqual(
            self.contrast_ratio("#cbd5e1", "#111827"),
            4.5,
        )

    def test_cyan_palette_is_consistent_across_app_theme_and_streamlit(self):
        project_root = Path(__file__).parent.parent
        style = (project_root / "static" / "style.css").read_text(encoding="utf-8")
        theme = (project_root / "app" / "theme.py").read_text(encoding="utf-8")
        config = (project_root / ".streamlit" / "config.toml").read_text(
            encoding="utf-8"
        )

        self.assertRegex(style, r"--brand-primary:\s*#0e7490\b")
        self.assertRegex(theme, r"--brand-primary:\s*#0e7490\b")
        self.assertRegex(config, r'primaryColor\s*=\s*"#0e7490"')
        self.assertRegex(style, r"--brand-primary-hover:\s*#155e75\b")
        self.assertRegex(style, r"--brand-secondary:\s*#6d28d9\b")
        self.assertRegex(style, r"--brand-accent:\s*#2563eb\b")

    def test_dark_heading_and_focus_tokens_have_visible_contrast(self):
        theme = (
            Path(__file__).parent.parent / "app" / "theme.py"
        ).read_text(encoding="utf-8")
        tokens = dict(
            re.findall(
                r"(--(?:brand-heading-start|focus-ring)):\s*(#[0-9a-fA-F]{6})",
                theme,
            )
        )

        for token in ("--brand-heading-start", "--focus-ring"):
            with self.subTest(token=token):
                self.assertIn(token, tokens)
                background = "#1e293b" if token == "--focus-ring" else "#0b1220"
                self.assertGreaterEqual(
                    self.contrast_ratio(tokens[token], background),
                    3.0,
                )

        text_tokens = dict(
            re.findall(
                r"(--brand-(?:primary|secondary|accent)-text):\s*(#[0-9a-fA-F]{6})",
                theme,
            )
        )
        for token in (
            "--brand-primary-text",
            "--brand-secondary-text",
            "--brand-accent-text",
        ):
            with self.subTest(token=token):
                self.assertIn(token, text_tokens)
                self.assertGreaterEqual(
                    self.contrast_ratio(text_tokens[token], "#111827"),
                    4.5,
                )

    def test_bundled_lucide_icons_have_local_accessible_svg_assets(self):
        for icon_name in ICON_NAMES:
            with self.subTest(icon_name=icon_name):
                svg = get_icon_svg(icon_name)

                self.assertIn("<svg ", svg)
                self.assertIn('aria-hidden="true"', svg)
                self.assertIn('stroke="currentColor"', svg)

    def test_icon_size_is_applied_to_svg_dimensions(self):
        svg = get_icon_svg("rocket", size=36)

        self.assertIn('width="36"', svg)
        self.assertIn('height="36"', svg)

    def test_unknown_icon_is_rejected(self):
        with self.assertRaises(ValueError):
            get_icon_svg("../main")

    def test_invalid_icon_size_is_rejected(self):
        for size in (15, 65, 24.5, True):
            with self.subTest(size=size):
                with self.assertRaises(ValueError):
                    # Preserve the invalid runtime value while satisfying the static API type.
                    get_icon_svg("house", size=cast(int, size))

    def test_icon_text_input_keeps_accessible_streamlit_label(self):
        with (
            mock.patch("app.ui.st.markdown") as markdown,
            mock.patch("app.ui.st.text_input", return_value="sample") as text_input,
        ):
            result = render_icon_text_input(
                "Email",
                "mail",
                key="email",
                placeholder="name@example.com",
            )

        self.assertEqual(result, "sample")
        self.assertIn("<svg ", markdown.call_args.args[0])
        self.assertIn("Email", markdown.call_args.args[0])
        self.assertEqual(text_input.call_args.args[0], "Email")
        self.assertEqual(text_input.call_args.kwargs["type"], "default")
        self.assertEqual(text_input.call_args.kwargs["label_visibility"], "collapsed")

    def test_icon_button_keeps_text_label_and_streamlit_button_behavior(self):
        icon_column, button_column = mock.MagicMock(), mock.MagicMock()
        with (
            mock.patch("app.ui.st.columns", return_value=(icon_column, button_column)),
            mock.patch("app.ui.st.markdown") as markdown,
            mock.patch("app.ui.st.button", return_value=True) as button,
        ):
            clicked = render_icon_button("Entrar", "log-in", key="login_submit")

        self.assertTrue(clicked)
        self.assertIn("<svg ", markdown.call_args.args[0])
        self.assertEqual(button.call_args.args[0], "Entrar")
        self.assertEqual(button.call_args.kwargs["key"], "login_submit")
        self.assertEqual(button.call_args.kwargs["type"], "secondary")
        self.assertFalse(button.call_args.kwargs["disabled"])

        with (
            mock.patch("app.ui.st.columns", return_value=(icon_column, button_column)),
            mock.patch("app.ui.st.markdown"),
            mock.patch("app.ui.st.button") as disabled_button,
        ):
            render_icon_button(
                "Ver Roadmap",
                "map",
                key="home-open-roadmap",
                disabled=True,
            )

        self.assertTrue(disabled_button.call_args.kwargs["disabled"])

    def test_button_group_applies_primary_button_type(self):
        columns = [mock.MagicMock(), mock.MagicMock()]
        with (
            mock.patch("app.ui.st.columns", return_value=columns),
            mock.patch("app.ui.st.button") as button,
        ):
            render_button_group(
                [
                    {"label": "Continuar", "key": "continue", "primary": True},
                    {"label": "Voltar", "key": "back"},
                ]
            )

        self.assertEqual(button.call_args_list[0].kwargs["type"], "primary")
        self.assertEqual(button.call_args_list[1].kwargs["type"], "secondary")

    def test_icon_text_input_accepts_password_type(self):
        with (
            mock.patch("app.ui.st.markdown"),
            mock.patch("app.ui.st.text_input", return_value="secret") as text_input,
        ):
            result = render_icon_text_input(
                "Senha",
                "key-round",
                key="password",
                placeholder="Digite sua senha",
                input_type="password",
            )

        self.assertEqual(result, "secret")
        self.assertEqual(text_input.call_args.kwargs["type"], "password")

    def test_shared_components_use_theme_tokens(self):
        with mock.patch("app.ui.st.markdown") as markdown:
            render_feature_card("Título", "Descrição", "brain", color="success")
            render_profile_badge("Estudante")
            render_quiz_progress(1, 5)
            render_roadmap_item("Fundamentos", 1)
            render_roadmap_item("Lógica", 2, is_completed=True)
            render_empty_state("Sem itens", "Adicione um material.")
            render_stat_card("Módulos", "13")

        rendered = "\n".join(call.args[0] for call in markdown.call_args_list)
        for token in (
            "var(--bg-surface)",
            "var(--border)",
            "var(--text-primary)",
            "var(--text-secondary)",
            "var(--text-on-brand)",
            "var(--brand-primary)",
            "var(--color-success)",
            "var(--shadow)",
        ):
            with self.subTest(token=token):
                self.assertIn(token, rendered)


if __name__ == "__main__":
    unittest.main()
