@user_router.callback_query(F.data == "middle")
async def middle_ex(callback:CallbackQuery, state:FSMContext):
    kb = SmartKeyboard(callback.from_user)
    kb.add_buttons([
    "print()",
    "split()",
    "lambda",
    "Docker",
    "Git",
    "API",
    "JSON",
    "SQL",
    "PostgreSQL",
    "FastAPI",
    "aiogram",
    "asyncio",
    "class",
    "inheritance",
    "polymorphism",
    "encapsulation",
    "recursion",
    "generator",
    "iterator",
    "decorator",
    "context manager",
    "try/except",
    "threading",
    "multiprocessing",
    "REST",
    "WebSocket",
    "ORM",
    "Redis",
    "Kubernetes",
    "CI/CD"
])
    kb.set_prop([3,4,3], 10, next_button="➡️", back_button="⬅️", home_button="menu")
    await state.set_state("smartKb")
    await callback.message.answer("Keyboard that contains 30 buttons in the order: 3 buttons, 4 buttons, 3 buttons", reply_markup=kb.get_keyboard())
    
@user_router.callback_query(F.data == "➡️")
async def next_kb_page_handker(callback:CallbackQuery):
    kb = SmartKeyboard(callback.from_user)
    await callback.message.edit_text(text="You have moved to the next page", reply_markup=kb.get_keyboard())

@user_router.callback_query(F.data == "⬅️")
async def previous_kb_page_handler(callback:CallbackQuery):
    kb = SmartKeyboard(callback.from_user)
    await callback.message.edit_text(text="You have gone back to the previous page ", reply_markup=kb.previous_keyboard())

@user_router.callback_query(F.data == "menu")
async def menu_handler(callback:CallbackQuery, state:FSMContext):
    if SmartKeyboard.check_user(callback.from_user):
        SmartKeyboard.delete_user(callback.from_user)
    await callback.message.answer("You're back at the menu", reply_markup=user_kb.start)
    await callback.message.delete()
    await state.clear()
