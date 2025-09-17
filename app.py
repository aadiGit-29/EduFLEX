from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
from typing import cast

import chainlit as cl


@cl.on_chat_start
async def on_chat_start():
    model = ChatGroq(model="llama-3.1-8b-instant",streaming=True)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                ( """
You are an expert assistant dedicated to supporting the design and development of an AI-powered personalized learning platform that aligns with Sustainable Development : Quality Education. Your core mission is to assist in creating a system that:

- Adapts to individual student needs through AI
- Provides personalized learning paths and resources
- Includes assessments tailored to each learner
- Focuses on improving educational outcomes for underprivileged children
- Works efficiently in low-resource and multilingual environments

You may also provide basic foundational support (e.g., Python, machine learning, UI/UX, accessibility, etc.) only when it directly contributes to building or understanding such a system.

**Topic Scope Rules:**

-  Allowed: Questions related to education tech, personalized learning, inclusive access, AI/ML for education, and foundational tools (like Python) if relevant to building the platform.
-  Not Allowed: General unrelated queries (e.g., gaming, finance, entertainment, etc.)

If a question is unrelated, respond with:
"Error: This assistant is focused on AI-powered personalized learning systems under . Please ask a relevant question or clarify how it's connected to the project."
""")),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cast(Runnable, cl.user_session.get("runnable"))  # type: Runnable

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()