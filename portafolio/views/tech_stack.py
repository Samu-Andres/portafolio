import reflex as rx
from portafolio.components.heading import heading
from portafolio.data import Technology
from portafolio.styles.styles import EmSize, Size


def tech_stack(technologies: list[Technology]) -> rx.Component:
    return rx.vstack(
        heading("Technologies"),
        rx.flex(
            *[
                rx.badge(
                    rx.box(
                        # Asegura que es string
                        class_name=str(technology.icon),
                        font_size="24px"
                    ),
                    rx.text(str(technology.name)),  # Asegura que es string
                    size="2"
                )
                for technology in technologies if isinstance(technology, Technology)
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )
