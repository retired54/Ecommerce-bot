# PRODUCT LIST

PRODUCT_IDS = [
    "tshirt", "men_Shoes", "women_Shoes", "children_Shoes", "men_jeans", "women_jeans", "children_jeans", "anyproducts"
]
PRODUCT_NAMES = {
    "tshirt":  "JC T SHIRT (PUT SIZE IN HUSHNOTE)",
    "men_Shoes": "MEN'S_SHOES",
    "women_Shoes": "WOMEN'S_SHOES",
    "children_Shoes":  "CHILDREN'S_SHOES",
    "men_jeans":  "MEN'S_JEANS",
    "women_jeans":  "WOMEN'S_JEANS",
    "children_jeans":  "CHILDREN'S_JEANS",
    
}

def product_list_kb() -> InlineKeyboardMarkup:
    rows = []
    for pid in PRODUCT_IDS:
        rows.append([InlineKeyboardButton(text=PRODUCT_NAMES[pid], callback_data=f"p:{pid}")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

@dp.message(F.text == "🛍️ Product Listings")
async def show_products_list(message: types.Message, state: FSMContext):
    if await state.get_state() != AuthStates.VERIFIED:
        await message.answer("Please /start and verify first.")
        return
    await message.answer("Choose a product:", reply_markup=product_list_kb())


# PRODUCT CARDS + VARIANTS

def add_variant_button(pid: str, label: str, price: float) -> InlineKeyboardButton:
    vid = new_vid()
    VARIANTS[vid] = (PRODUCT_NAMES[pid], label, price)
    return InlineKeyboardButton(text=f"Add {label} - ${price}", callback_data=f"add:{vid}")
