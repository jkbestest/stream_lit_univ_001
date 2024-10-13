
import streamlit as st

print("page reloaded")
st.set_page_config(
    page_title="포켓몬 도감",
    page_icon="monsterball.png"
)
st.markdown("""
<style>
img {
    max-height: 300px;
}
.streamlit-expanderContent div{
    display: flex;
    justify-content: center;
    font-size: 20px;
}
[data-testid="stExpanderToggleIcon"] {
    visibility: hidden;
}
.streamlit-expanderHeader {
    pointer-events: none;
}

[data-testid="StyledFullScreenButton] {
    visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

st.title("Pokemon Dictionary")

st.text("포켓몬을 하나씩 추가해서 도감을 만들어 보세요!")
type_emoji_dict = {
    "노말": "⚪",
    "격투": "✊",
    "비행": "🕊",
    "독": "☠️",
    "땅": "🌋",
    "바위": "🪨",
    "벌레": "🐛",
    "고스트": "👻",
    "강철": "🤖",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "에스퍼": "🔮",
    "얼음": "❄️",
    "드래곤": "🐲",
    "악": "😈",
    "페어리": "🧚"
}

initial_pokemons = [
    {
        "name": "이상해씨",
        "types": ["풀", "독"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/000101.png"
    },
    {
        "name": "이상해풀",
        "types": ["풀", "독"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/000201.png"
    },
    {
        "name": "이상해꽃",
        "types": ["풀", "독"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/000301.png"
    },
    {
        "name": "파이리",
        "types": ["불꽃"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/000401.png"
    },
    {
        "name": "리자드",
        "types": ["불꽃"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/000501.png"
    },
    {
        "name": "리자몽",
        "types": ["불꽃", "비행"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/000601.png"
    },
    {
        "name": "꼬부기",
        "types": ["물"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/000701.png"
    },
    {
        "name": "어니부기",
        "types": ["물"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/000801.png"
    },
    {
        "name": "거북왕",
        "types": ["물"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/000901.png"
    },
    {
        "name": "캐터피",
        "types": ["벌레"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/001001.png"
    },
    {
        "name": "단데기",
        "types": ["벌레"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/001101.png"
    },
    {
        "name": "버터플",
        "types": ["벌레", "비행"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/001201.png"
    },
    {
        "name": "뿔충이",
        "types": ["벌레", "독"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/001301.png"
    },
    {
        "name": "딱충이",
        "types": ["벌레", "독"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/001401.png"
    },
    {
        "name": "독침붕",
        "types": ["벌레", "독"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/001501.png"
    },
    {
        "name": "구구",
        "types": ["노말", "비행"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/001601.png"
    },
    {
        "name": "피죤",
        "types": ["노말", "비행"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/001701.png"
    },
    {
        "name": "피죤투",
        "types": ["노말", "비행"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/001801.png"
    },
    {
        "name": "꼬렛",
        "types": ["노말"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/001901.png"
    },
    {
        "name": "레트라",
        "types": ["노말"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/002001.png"
    },
    {
        "name": "깨비참",
        "types": ["노말", "비행"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/002101.png"
    },
    {
        "name": "깨비드릴조",
        "types": ["노말", "비행"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/002201.png"
    },
    {
        "name": "아보",
        "types": ["독"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/002301.png"
    },
    {
        "name": "아보크",
        "types": ["독"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/002401.png"
    },
    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/pikachu.webp"
    },
    {
        "name": "라이츄",
        "types": ["전기"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/002601.png"
    },
    {
        "name": "모래두지",
        "types": ["땅"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/002701.png"
    },
    {
        "name": "고지",
        "types": ["땅"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/002801.png"
    },
    {
        "name": "니드런♀",
        "types": ["독"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/002901.png"
    },
    {
        "name": "니드리나",
        "types": ["독"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/003001.png"
    },
    {
        "name": "니드퀸",
        "types": ["독", "땅"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/003101.png"
    },
    {
        "name": "니드런♂",
        "types": ["독"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/003201.png"
    },
    {
        "name": "니드리노",
        "types": ["독"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/003301.png"
    },
    {
        "name": "니드킹",
        "types": ["독", "땅"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/003401.png"
    },
    {
        "name": "삐삐",
        "types": ["페어리"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/003501.png"
    },
    {
        "name": "픽시",
        "types": ["페어리"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/003601.png"
    },
    {
        "name": "식스테일",
        "types": ["불꽃"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/003701.png"
    },
    {
        "name": "나인테일",
        "types": ["불꽃"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/003801.png"
    },
    {
        "name": "푸린",
        "types": ["노말", "페어리"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/003901.png"
    },
    {
        "name": "푸크린",
        "types": ["노말", "페어리"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/004001.png"
    },
    {
        "name": "주뱃",
        "types": ["독", "비행"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/004101.png"
    },
    {
        "name": "골뱃",
        "types": ["독", "비행"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/004201.png"
    },
    {
        "name": "뚜벅쵸",
        "types": ["풀", "독"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/004301.png"
    },
    {
        "name": "냄새꼬",
        "types": ["풀", "독"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/004401.png"
    },
    {
        "name": "라플레시아",
        "types": ["풀", "독"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/004501.png"
    },
    {
        "name": "파라스",
        "types": ["벌레", "풀"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/004601.png"
    },
    {
        "name": "파라섹트",
        "types": ["벌레", "풀"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/004701.png"
    },
    {
        "name": "콘팡",
        "types": ["벌레", "독"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/004801.png"
    },
    {
        "name": "도나리",
        "types": ["벌레", "독"],
        "image_url": "https://data1.pokemonkorea.co.kr/newdata/pokedex/mid/004901.png"
    }
]


example_pokemon = {
    "name": "알로라 디그다",
    "types": ["강철", "땅"],
    "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/alora_digda.webp"
}

if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons

auto_complete = st.toggle("예시 데이터로 채우기")
print("page_reload, auto_complete", auto_complete)


with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
            label="포켓몬 이름",
            value=example_pokemon["name"] if auto_complete else ""
            )
    with col2:
        types = st.multiselect(
            label="포켓몬 속성",
            options=list(type_emoji_dict.keys()),
            max_selections=2,
            default=example_pokemon["types"] if auto_complete else []
        )
    image_url = st.text_input(
        label="포켓몬 이미지 URL",
        value=example_pokemon["image_url"] if auto_complete else ""
        )
    submit = st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("포켓몬의 이름을 입력해 주세요!")
        elif len(types) == 0:
            st.error("포켓몬의 속성을 적어도 한 개 선택해주세요!")
        else:
            st.success("포켓몬을 추가할 수 있습니다.") 
            st.session_state.pokemons.append({
                "name": name,
                "types": types,
                "image_url":image_url if image_url else "default.png"
            })


for i in range(0, len(st.session_state.pokemons), 3):
    row_pokemons = st.session_state.pokemons[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label= f"**{i+j+1}. {pokemon["name"]}**", expanded=True):
                st.image(pokemon["image_url"])
                emoji_types= [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                st.text(" / ".join(emoji_types))
                delete_button = st.button(
                    label="삭제", key=i+j,
                    use_container_width=True
                    )
                if delete_button:
                    print("delete button clicked!")
                    del st.session_state.pokemons[i+j]
                    st.rerun()


st.write("**Operator Name: Jun Gi Hwang, Insta: @___hwjk**")


