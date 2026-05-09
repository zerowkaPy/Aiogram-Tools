
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.types.user import User



class SmartKeyboard:
    _instance = {}  # {user_id : instance}

    def __new__(cls, from_user: User):
        user_id = str(from_user.id)
        if user_id in cls._instance:
            return cls._instance[user_id]
        instance = super().__new__(cls)
        cls._instance[user_id] = instance
        return instance

    def __init__(self, user_id):
        if hasattr(self, "_initialized"):
            return
        self.__user_id = str(user_id)
        self.__initialized = True  # флаг ініціалізації екземпляру
        self.__kb_init = False #флаг ініціалізації клавіатури

    def init_keyboard(self):
        self.__adjust = None
        self.__buttons = None
        self.__page_num = None
        self.__rest = None
        self.__rows_num = None
        self.__next_button = None
        self.__back_button = None
        self.__home_button = None
        self.__pages = {}
        self.__pages_prop = {}
        self.__count = 1

        self.__kb_init = True


    def __kb_prop(self):
        self.__page_num = len(self.__buttons) // self.__rows_num
        self.__rest = len(self.__buttons) % self.__rows_num

        if self.__rest:
            self.__page_num = self.__page_num+1

    def __prop_check(self):
        if self.__adjust:
            return True
        else:
            return False

    def set_prop(self, adjust:list[int], rows_num:int, next_button:str = "next", back_button:str = "back", home_button :str = None):
        if not self.__buttons:
            raise SyntaxError("you must first execute 'add_buttons'")
        self.__adjust = adjust
        self.__rows_num = rows_num
        self.__next_button = next_button
        self.__back_button = back_button
        self.__home_button = home_button
        self.__kb_prop()

        for page in range(self.__page_num):
            page +=1
            self.__pages[str(page)] = [button for button in self.__buttons[:self.__rows_num]]
            self.__buttons = self.__buttons[self.__rows_num:]
            self.__last_page = page

        if self.__rest:
            self.__pages[str(self.__last_page+1)] = [button for button in self.__buttons]
            self.__buttons.clear()

        for page in range(self.__page_num):
            page+=1
            if self.__page_num == 1 and self.__rest == 0:
                self.__pages_prop[str(page)] = "none"
            elif page == 1:
                self.__pages_prop[str(page)] = "n"
            elif self.__page_num - page == 0 and self.__rest:
                self.__pages_prop[str(page)] = 'b'
            elif self.__page_num - page == 0:
                self.__pages_prop[str(page)] = "b"
            else:
                self.__pages_prop[str(page)] = "bn"


    def add_butons(self, buttons:list[str]):
        if not self.__kb_init:
            raise RuntimeError("you must execute init_keyboard before call add_butons")
        if type(buttons) != list:
            raise TypeError("buttons parameter must be a list of strings")
        if len(buttons) == 0:
            raise ValueError("buttons parameter must contain at least 1 string")
        self.__buttons = buttons

        self.__kb_init = False

        
    def get_keyboard(self):
        if self.__prop_check():
            builder = InlineKeyboardBuilder()
            page = self.__pages_prop[str(self.__count)]
            if page == 'none':
                for button in self.__pages[str(self.__count)]:
                    builder.add(InlineKeyboardButton(text=button, callback_data=button))
                builder.adjust(*self.__adjust)
                adjust = [*self.__adjust]
                self.__count +=1
            elif page == 'n':
                for button in self.__pages[str(self.__count)]:
                    builder.add(InlineKeyboardButton(text=button, callback_data=button))
                builder.add(InlineKeyboardButton(text=self.__next_button, callback_data=self.__next_button))
                builder.adjust(*self.__adjust, 1)
                adjust = [*self.__adjust, 1]
                self.__count +=1
            elif page == 'bn':
                for button in self.__pages[str(self.__count)]:
                    builder.add(InlineKeyboardButton(text=button, callback_data=button))
                builder.add(InlineKeyboardButton(text=self.__next_button, callback_data=self.__next_button))
                builder.add(InlineKeyboardButton(text=self.__back_button, callback_data=self.__back_button))
                builder.adjust(*self.__adjust, 2)
                adjust = [*self.__adjust, 2]
                self.__count +=1
            elif page == 'b':
                for button in self.__pages[str(self.__count)]:
                    builder.add(InlineKeyboardButton(text=button, callback_data=button))
                builder.add(InlineKeyboardButton(text=self.__back_button, callback_data=self.__back_button))
                builder.adjust(*self.__adjust, 1)
                adjust = [*self.__adjust, 1]
                self.__count +=1

            if self.__home_button:
                builder.add(InlineKeyboardButton(text=self.__home_button, callback_data=self.__home_button))
                builder.adjust(*adjust, 1)
            return builder.as_markup()
        else:
            raise RuntimeError("You must execute set_prop() before calling get_keyboard()")
        
    def previous_keyboard(self):
        builder = InlineKeyboardBuilder()
        count = self.__count - 2
        self.__count -=1
        page = self.__pages_prop[str(count)]
        if page == 'n':
            for button in self.__pages[str(count)]:
                builder.add(InlineKeyboardButton(text=button, callback_data=button))
            builder.add(InlineKeyboardButton(text=self.__next_button, callback_data=self.__next_button))
            builder.adjust(*self.__adjust, 1)
            adjust = [*self.__adjust, 1]
        elif page == 'bn':
            for button in self.__pages[str(count)]:
                builder.add(InlineKeyboardButton(text=button, callback_data=button))
            builder.add(InlineKeyboardButton(text=self.__next_button, callback_data=self.__next_button))
            builder.add(InlineKeyboardButton(text=self.__back_button, callback_data=self.__back_button))
            builder.adjust(*self.__adjust, 2)
            adjust = [*self.__adjust, 2]

        if self.__home_button:
                builder.add(InlineKeyboardButton(text=self.__home_button, callback_data=self.__home_button))
                builder.adjust(*adjust, 1)
        return builder.as_markup()
