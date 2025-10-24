#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daily Advanced Vocabulary Blog Post Generator
2024-03-22 ~ 2025-10-19까지 매일 고급 영단어 포스트 생성
"""

import os
from datetime import datetime, timedelta
import random

# 고급 영단어 데이터베이스
ADVANCED_VOCABULARY = [
    # Week 1: Academic & Intellectual Words
    {
        "word": "Perspicacious",
        "pronunciation": "/ˌpɜːspɪˈkeɪʃəs/",
        "meaning": "통찰력 있는, 예리한",
        "definition": "Having keen insight and discernment",
        "examples": [
            "Her perspicacious analysis of the market trends helped the company avoid major losses.",
            "The perspicacious detective noticed the subtle clues others had missed."
        ],
        "synonyms": ["astute", "shrewd", "perceptive"],
        "word_family": {
            "noun": "perspicacity",
            "adverb": "perspicaciously"
        }
    },
    {
        "word": "Erudite",
        "pronunciation": "/ˈerʊdaɪt/",
        "meaning": "박학한, 학식이 깊은",
        "definition": "Having or showing great knowledge acquired by study",
        "examples": [
            "The professor's erudite lecture covered centuries of philosophical thought.",
            "His erudite commentary on classical literature impressed the scholars."
        ],
        "synonyms": ["learned", "scholarly", "knowledgeable"],
        "word_family": {
            "noun": "erudition",
            "adverb": "eruditely"
        }
    },
    {
        "word": "Cogent",
        "pronunciation": "/ˈkoʊdʒənt/",
        "meaning": "설득력 있는, 논리적인",
        "definition": "Clear, logical, and convincing",
        "examples": [
            "She presented a cogent argument for increasing the education budget.",
            "The lawyer's cogent reasoning swayed the jury."
        ],
        "synonyms": ["compelling", "persuasive", "convincing"],
        "word_family": {
            "noun": "cogency",
            "adverb": "cogently"
        }
    },
    {
        "word": "Sagacious",
        "pronunciation": "/səˈɡeɪʃəs/",
        "meaning": "현명한, 지혜로운",
        "definition": "Having good judgment; wise",
        "examples": [
            "The sagacious elder gave advice that proved invaluable.",
            "Her sagacious investment decisions made her wealthy."
        ],
        "synonyms": ["wise", "prudent", "judicious"],
        "word_family": {
            "noun": "sagacity",
            "adverb": "sagaciously"
        }
    },
    {
        "word": "Articulate",
        "pronunciation": "/ɑːrˈtɪkjələt/",
        "meaning": "표현이 명확한, 유창한",
        "definition": "Fluent and coherent in speech",
        "examples": [
            "The articulate speaker captivated the entire audience.",
            "She was surprisingly articulate for someone so young."
        ],
        "synonyms": ["eloquent", "fluent", "well-spoken"],
        "word_family": {
            "verb": "articulate",
            "noun": "articulation",
            "adverb": "articulately"
        }
    },
    # Week 2: Emotional & Psychological Words
    {
        "word": "Melancholy",
        "pronunciation": "/ˈmelənkɒli/",
        "meaning": "우울한, 슬픈",
        "definition": "A pensive sadness or thoughtful sorrow",
        "examples": [
            "The melancholy music perfectly captured his mood.",
            "She felt a deep melancholy as autumn arrived."
        ],
        "synonyms": ["sorrowful", "pensive", "wistful"],
        "word_family": {
            "adjective": "melancholic",
            "adverb": "melancholically"
        }
    },
    {
        "word": "Euphoric",
        "pronunciation": "/juːˈfɒrɪk/",
        "meaning": "행복감에 취한, 도취된",
        "definition": "Characterized by intense excitement and happiness",
        "examples": [
            "The team was euphoric after winning the championship.",
            "She felt euphoric when she received the job offer."
        ],
        "synonyms": ["elated", "ecstatic", "jubilant"],
        "word_family": {
            "noun": "euphoria",
            "adverb": "euphorically"
        }
    },
    {
        "word": "Nostalgic",
        "pronunciation": "/nɒˈstældʒɪk/",
        "meaning": "향수에 젖은, 그리워하는",
        "definition": "Feeling sentimental longing for the past",
        "examples": [
            "Looking at old photos made her feel nostalgic.",
            "The nostalgic song brought back childhood memories."
        ],
        "synonyms": ["wistful", "sentimental", "reminiscent"],
        "word_family": {
            "noun": "nostalgia",
            "adverb": "nostalgically"
        }
    },
    {
        "word": "Resilient",
        "pronunciation": "/rɪˈzɪliənt/",
        "meaning": "회복력이 있는, 탄력적인",
        "definition": "Able to recover quickly from difficulties",
        "examples": [
            "Children are remarkably resilient in the face of adversity.",
            "The resilient economy bounced back from the recession."
        ],
        "synonyms": ["adaptable", "flexible", "robust"],
        "word_family": {
            "noun": "resilience",
            "adverb": "resiliently"
        }
    },
    {
        "word": "Contemplative",
        "pronunciation": "/kənˈtemplətɪv/",
        "meaning": "사색적인, 명상적인",
        "definition": "Expressing or involving deep thought",
        "examples": [
            "She sat in contemplative silence by the lake.",
            "His contemplative nature made him a good philosopher."
        ],
        "synonyms": ["thoughtful", "reflective", "meditative"],
        "word_family": {
            "verb": "contemplate",
            "noun": "contemplation",
            "adverb": "contemplatively"
        }
    },
    # Continue with more categories...
    {
        "word": "Ubiquitous",
        "pronunciation": "/juːˈbɪkwɪtəs/",
        "meaning": "어디에나 있는, 편재하는",
        "definition": "Present everywhere simultaneously",
        "examples": [
            "Smartphones have become ubiquitous in modern society.",
            "The ubiquitous presence of advertising affects our daily choices."
        ],
        "synonyms": ["omnipresent", "pervasive", "widespread"],
        "word_family": {
            "noun": "ubiquity",
            "adverb": "ubiquitously"
        }
    },
    {
        "word": "Serendipity",
        "pronunciation": "/ˌserənˈdɪpəti/",
        "meaning": "뜻밖의 발견, 우연한 행운",
        "definition": "A pleasant surprise or fortunate accident",
        "examples": [
            "Meeting her mentor at the conference was pure serendipity.",
            "Many scientific discoveries happen through serendipity."
        ],
        "synonyms": ["fortuity", "chance", "luck"],
        "word_family": {
            "adjective": "serendipitous",
            "adverb": "serendipitously"
        }
    },
    {
        "word": "Ephemeral",
        "pronunciation": "/ɪˈfemərəl/",
        "meaning": "일시적인, 덧없는",
        "definition": "Lasting for a very short time",
        "examples": [
            "The ephemeral beauty of cherry blossoms is deeply moving.",
            "Internet fame can be quite ephemeral."
        ],
        "synonyms": ["transient", "fleeting", "temporary"],
        "word_family": {
            "noun": "ephemerality",
            "adverb": "ephemerally"
        }
    },
    {
        "word": "Meticulous",
        "pronunciation": "/məˈtɪkjələs/",
        "meaning": "세심한, 꼼꼼한",
        "definition": "Showing great attention to detail",
        "examples": [
            "Her meticulous research impressed the review committee.",
            "The surgeon's meticulous technique saved the patient."
        ],
        "synonyms": ["careful", "thorough", "precise"],
        "word_family": {
            "noun": "meticulousness",
            "adverb": "meticulously"
        }
    },
    {
        "word": "Paradigm",
        "pronunciation": "/ˈperəˌdaɪm/",
        "meaning": "패러다임, 모형",
        "definition": "A typical example or pattern of something",
        "examples": [
            "The internet created a new paradigm for communication.",
            "We need a paradigm shift in our approach to education."
        ],
        "synonyms": ["model", "framework", "archetype"],
        "word_family": {
            "adjective": "paradigmatic",
            "adverb": "paradigmatically"
        }
    }
    # Add more words here - we'll expand this list
]

def generate_more_vocabulary():
    """Generate additional vocabulary to reach target number"""
    additional_words = [
        {
            "word": "Magnanimous",
            "pronunciation": "/mæɡˈnænəməs/",
            "meaning": "관대한, 고결한",
            "definition": "Generous in forgiving; noble and generous in spirit",
            "examples": [
                "The magnanimous leader pardoned his former enemies.",
                "Her magnanimous gesture won the respect of all."
            ],
            "synonyms": ["generous", "noble", "charitable"],
            "word_family": {
                "noun": "magnanimity",
                "adverb": "magnanimously"
            }
        },
        {
            "word": "Tenacious",
            "pronunciation": "/təˈneɪʃəs/",
            "meaning": "끈질긴, 고집스러운",
            "definition": "Holding fast; persistent",
            "examples": [
                "Her tenacious pursuit of justice never wavered.",
                "The tenacious vine clung to the old wall."
            ],
            "synonyms": ["persistent", "determined", "stubborn"],
            "word_family": {
                "noun": "tenacity",
                "adverb": "tenaciously"
            }
        },
        {
            "word": "Immaculate",
            "pronunciation": "/ɪˈmækjələt/",
            "meaning": "완벽한, 흠없는",
            "definition": "Perfectly clean, neat, or tidy",
            "examples": [
                "His immaculate appearance impressed the interviewers.",
                "The house was kept in immaculate condition."
            ],
            "synonyms": ["spotless", "flawless", "pristine"],
            "word_family": {
                "adverb": "immaculately"
            }
        }
        # Continue adding more words...
    ]

    return ADVANCED_VOCABULARY + additional_words

def create_daily_post(date, word_data, post_number):
    """Create a daily vocabulary post"""

    # Format date
    date_str = date.strftime("%Y-%m-%d")
    formatted_date = date.strftime("%Y-%m-%d %H:%M:%S +0900")
    korean_date = date.strftime("%m월 %d일")

    # Get word information
    word = word_data["word"]
    pronunciation = word_data["pronunciation"]
    meaning = word_data["meaning"]
    definition = word_data["definition"]
    examples = word_data["examples"]
    synonyms = word_data.get("synonyms", [])
    word_family = word_data.get("word_family", {})

    # Create post content
    content = f"""---
layout: post
title: "Daily Advanced Vocabulary #{post_number}: {word}"
date: {formatted_date}
categories: [Vocabulary, Advanced English, Daily Learning]
tags: [advanced vocabulary, daily learning, {word.lower()}, english fluency]
---

# 📚 **매일 배우는 고급 영단어 #{post_number}**

## 🌟 **오늘의 단어 ({korean_date})**

### **{word}** {pronunciation}

**한국어 뜻**: {meaning}
**영어 정의**: {definition}

<!--more-->

---

## 📖 **예문 (Examples)**

"""

    for i, example in enumerate(examples, 1):
        content += f"**{i}.** *{example}*\n\n"

    if synonyms:
        content += f"**동의어 (Synonyms)**: {', '.join(synonyms)}\n\n"

    if word_family:
        content += "**어족 (Word Family)**:\n"
        for pos, form in word_family.items():
            content += f"- {pos.capitalize()}: {form}\n"
        content += "\n"

    content += f"""---

## 🎯 **활용 연습 (Practice)**

다음 빈칸에 오늘 배운 단어를 적절한 형태로 넣어보세요:

1. The _______ attention to detail made the project successful.
2. Her _______ approach to problem-solving impressed everyone.

*(정답은 포스트 하단에 있습니다)*

---

## 💡 **학습 팁 (Learning Tip)**

**연상법 활용하기**: "{word}"를 기억하기 위해 개인적인 경험이나 이미지와 연결해보세요.
예를 들어, 이 단어가 사용된 상황을 구체적으로 상상하거나, 비슷한 소리의 한국어 단어와 연관지어 기억하는 방법이 효과적입니다.

---

## 📝 **오늘의 과제**

1. **문장 만들기**: 오늘 배운 단어를 사용해 3개의 문장을 만들어보세요.
2. **실제 사용**: 오늘 하루 동안 이 단어를 실제 대화나 글쓰기에서 1번 이상 사용해보세요.
3. **복습**: 어제 배운 단어와 함께 사용할 수 있는 문장을 만들어보세요.

---

## 🎲 **재미있는 사실 (Fun Fact)**

"{word}" 단어는 """

    # Add interesting etymology or usage facts
    if word.lower() in ["serendipity"]:
        content += "호레이스 월폴(Horace Walpole)이 1754년에 만든 단어로, 페르시아 동화 '세렌디프의 세 왕자'에서 따온 것입니다."
    elif word.lower() in ["ubiquitous"]:
        content += "라틴어 'ubique'(어디든지)에서 유래되었으며, 원래는 종교적 맥락에서 신의 편재성을 나타내는 데 사용되었습니다."
    else:
        content += f"학술적 글쓰기와 비즈니스 상황에서 자주 사용되는 고급 어휘입니다. 이 단어를 적절히 사용하면 영어 실력이 한층 업그레이드됩니다."

    content += f"""

---

## 📊 **진도 체크**

- **총 학습 단어**: {post_number}개
- **이번 주 목표**: 매일 1개씩 꾸준히 학습하기 ✅
- **누적 어휘**: 고급 영단어 {post_number}개 완료!

---

## ✅ **연습 문제 정답**

1. The **{word.lower()}** attention to detail made the project successful.
2. Her **{word.lower()}** approach to problem-solving impressed everyone.

---

**🎯 내일 예고**: 내일은 또 다른 유용한 고급 영단어를 배워보겠습니다. 꾸준한 학습으로 어휘력을 향상시켜 나가요!

**💭 오늘의 질문**: 오늘 배운 단어 "{word}"를 어떤 상황에서 사용해보고 싶으신가요?

Happy Learning! ✨📚

---

*매일 고급 영단어 시리즈는 체계적인 어휘 학습을 통해 영어 실력 향상을 돕는 연재입니다.*
"""

    return content

def generate_all_posts():
    """Generate all daily vocabulary posts from 2024-03-22 to 2025-10-19"""

    # Get extended vocabulary list
    vocabulary_list = generate_more_vocabulary()

    # Calculate date range
    start_date = datetime(2024, 3, 22)
    end_date = datetime(2025, 10, 19)

    current_date = start_date
    post_number = 1
    word_index = 0

    posts_dir = "_posts"
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)

    print(f"Starting to generate posts from {start_date.date()} to {end_date.date()}")
    print(f"Total vocabulary available: {len(vocabulary_list)} words")

    while current_date <= end_date:
        # Cycle through vocabulary if we run out
        if word_index >= len(vocabulary_list):
            word_index = 0
            # Shuffle for variety if cycling
            random.shuffle(vocabulary_list)

        word_data = vocabulary_list[word_index]

        # Create post content
        post_content = create_daily_post(current_date, word_data, post_number)

        # Create filename
        filename = f"{current_date.strftime('%Y-%m-%d')}-daily-advanced-vocabulary-{post_number}.md"
        filepath = os.path.join(posts_dir, filename)

        # Write post to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(post_content)

        print(f"Created post #{post_number}: {word_data['word']} ({current_date.date()})")

        # Move to next day
        current_date += timedelta(days=1)
        post_number += 1
        word_index += 1

    print(f"\\nCompleted! Generated {post_number - 1} posts.")
    print(f"Posts saved in '{posts_dir}' directory")

if __name__ == "__main__":
    generate_all_posts()