from pathlib import Path

import customtkinter as ctk
from PIL import Image


WINDOW_WIDTH = 450
WINDOW_HEIGHT = 700
BACKGROUND = "#F5EBDD"
INK = "#59483F"


class CatLedgerTitle(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("냥냥 가계부")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)
        self.configure(fg_color=BACKGROUND)

        self._cat_image: ctk.CTkImage | None = None

        self.title_label = ctk.CTkLabel(
            self,
            text="냥냥 가계부",
            font=ctk.CTkFont(family="맑은 고딕", size=34, weight="bold"),
            text_color=INK,
        )
        self.title_label.pack(pady=(42, 4))

        self.subtitle_label = ctk.CTkLabel(
            self,
            text="오늘도 밥그릇을 지켜줘!",
            font=ctk.CTkFont(family="맑은 고딕", size=16),
            text_color="#9A7965",
        )
        self.subtitle_label.pack(pady=(0, 24))

        self.cat_card = ctk.CTkFrame(
            self,
            width=350,
            height=350,
            corner_radius=30,
            fg_color="#FFFCF7",
            border_width=2,
            border_color="#E9D7C3",
        )
        self.cat_card.pack()
        self.cat_card.pack_propagate(False)

        self.show_cat_image_or_placeholder()

        self.start_button = ctk.CTkButton(
            self,
            text="게임 시작하기",
            command=self.start_game,
            width=300,
            height=58,
            corner_radius=24,
            font=ctk.CTkFont(family="맑은 고딕", size=18, weight="bold"),
            fg_color="#E99A83",
            hover_color="#D9836D",
            text_color="#FFFFFF",
        )
        self.start_button.pack(pady=(30, 12))

        self.goal_button = ctk.CTkButton(
            self,
            text="목표 예산 설정",
            width=300,
            height=54,
            corner_radius=24,
            font=ctk.CTkFont(family="맑은 고딕", size=17, weight="bold"),
            fg_color="#E8CF9C",
            hover_color="#D9BE88",
            text_color=INK,
        )
        self.goal_button.pack()

    def show_cat_image_or_placeholder(self) -> None:
        image_path = Path(__file__).with_name("cat_happy.png")
        if image_path.is_file():
            try:
                # Example: cat_image = Image.open("cat_happy.png")
                with Image.open(image_path) as source:
                    image = source.copy()
                self._cat_image = ctk.CTkImage(
                    light_image=image,
                    dark_image=image,
                    size=(280, 280),
                )
                ctk.CTkLabel(
                    self.cat_card,
                    text="",
                    image=self._cat_image,
                ).pack(expand=True)
                return
            except OSError as error:
                print(f"고양이 이미지를 불러오지 못했습니다: {error}")

        ctk.CTkLabel(
            self.cat_card,
            text="🐱 3D 고양이 이미지 영역",
            font=ctk.CTkFont(family="맑은 고딕", size=17, weight="bold"),
            text_color="#A58B78",
        ).pack(expand=True)

    def start_game(self) -> None:
        print("게임 시작하기 버튼을 눌렀습니다.")


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    app = CatLedgerTitle()
    app.mainloop()
