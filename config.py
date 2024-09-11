TOKEN = "7191775713:AAEksCJNWBjsNFbXanDKYLU4YueC_h526z4"
DELETE_DELAY = 5

CHAR_REPLACEMENTS = {
    'а': '[аa@]', 'б': '[бb6]', 'в': '[вv]', 'г': '[гg]', 'д': '[дd]',
    'е': '[еe3]', 'ё': '[ёe]', 'ж': '[жzh]', 'з': '[зz3]', 'и': '[иi1!]',
    'й': '[йi1]', 'к': '[кk]', 'л': '[лl]', 'м': '[мm]', 'н': '[нh]',
    'о': '[оo0(){}<>]', 'п': '[пn]', 'р': '[рp]', 'с': '[сc]', 'т': '[тt]',
    'у': '[уy]', 'ф': '[фf]', 'х': '[хx]', 'ц': '[цc]', 'ч': '[чch4]',
    'ш': '[шsh]', 'щ': '[щsch]', 'ы': '[ыy]', 'э': '[эe]', 'ю': '[юyu]',
    'я': '[яya]', ' ': r'\s*'
}

FORBIDDEN_WORDS = [
    "чурка", "жид", "путин", "хохлы", "зеленский", "какол", "svo",
    "коклек", "коклик", "война", "бомба", "cock", "путлер", "каклише",
    "геноцид", "терроризм", "оккупация", "путинский режим", "рашисты",
    "российская агрессия", "как теперь резатся", "хохлушес", "хохлес",
    "вагнер", "чвк", "бомбардировка", "свастика", "нацист", "русофобия",
    "химическое оружие", "танк", "оружие", "ель коклус", "кацап", "я режусь",
    "режусь", "режу вены", "луганск", "мариуполь", "сепаратисты", "нацистская россия",
    "военное преступление", "санкции", "коклесами", "эмбарго", "эвакуация",
    "провокация", "диверсия", "шпион", "агент", "агрессор", "кровопролитие",
    "антивоенный", "против войны", "война россии", "война на украине",
    "милитаризация", "мобилизация", "армия россии", "спецоперация",
    "путинская пропаганда", "пропаганда", "расстрел", "ядерное оружие",
    "боевые действия", "оккупационные войска", "патриотизм", "Х()х()л",
    "независимость украины", "денацификация", "милитаризм", "военный конфликт",
    "смертельный исход", "вражеские действия", "Хохохол", "революция",
    "нападение", "террористическая угроза", "политическая нестабильность",
    "завоевание", "силовая операция", "военное положение", "спецслужбы",
    "военное давление", "военная пропаганда", "хохл",
    "милитаристская риторика", "карательная операция", "нацификация",
    "тоталитаризм", "диктатура", "автократия", "государственный переворот"
]

FORBIDDEN_PHRASES = [
    "заявки принимаем сразу", "лучший канал по ставкам", "экспрессы сезона",
    "только высокие кэффы", "проводим розыгрыши", "вступай к нам",
    "регистрация по ссылке", "только лучшие предложения", "подключайся сейчас",
    "бесплатные прогнозы", "только у нас", "гарантируем победу",
    "быстрые выплаты", "зарабатывай с нами", "секретные стратегии",
    "максимальные шансы", "ставки на спорт", "получи бонус",
    "присоединяйся сейчас", "хохол"
]

URL_REGEX = r'(https?://\S+|t\.me/\S+)'

HEROES = [
    "Abaddon", "Alchemist", "Ancient Apparition", "Anti-Mage", "Arc Warden", "Axe",
    "Bane", "Batrider", "Beastmaster", "Bloodseeker", "Bounty Hunter", "Brewmaster",
    "Bristleback", "Broodmother", "Centaur Warrunner", "Chaos Knight", "Chen",
    "Clinkz", "Clockwerk", "Crystal Maiden", "Dark Seer", "Dark Willow", "Dawnbreaker",
    "Dazzle", "Death Prophet", "Disruptor", "Doom", "Dragon Knight", "Drow Ranger",
    "Earth Spirit", "Earthshaker", "Elder Titan", "Ember Spirit", "Enchantress",
    "Enigma", "Faceless Void", "Grimstroke", "Gyrocopter", "Hoodwink", "Huskar",
    "Invoker", "Io", "Jakiro", "Juggernaut", "Keeper of the Light", "Kunkka",
    "Legion Commander", "Leshrac", "Lich", "Lifestealer", "Lina", "Lion",
    "Lone Druid", "Luna", "Lycan", "Magnus", "Marci", "Mars", "Medusa", "Meepo",
    "Mirana", "Monkey King", "Morphling", "Muerta", "Naga Siren", "Nature's Prophet",
    "Necrophos", "Night Stalker", "Nyx Assassin", "Ogre Magi", "Omniknight",
    "Oracle", "Outworld Destroyer", "Pangolier", "Phantom Assassin", "Phantom Lancer",
    "Phoenix", "Primal Beast", "Puck", "Pudge", "Pugna", "Queen of Pain", "Razor",
    "Riki", "Ringmaster", "Rubick", "Sand King", "Shadow Demon", "Shadow Fiend",
    "Shadow Shaman", "Silencer", "Skywrath Mage", "Slardar", "Slark", "Snapfire",
    "Sniper", "Spectre", "Spirit Breaker", "Storm Spirit", "Sven", "Techies",
    "Templar Assassin", "Terrorblade", "Tidehunter", "Timbersaw", "Tinker",
    "Tiny", "Treant Protector", "Troll Warlord", "Tusk", "Underlord", "Undying",
    "Ursa", "Vengeful Spirit", "Venomancer", "Viper", "Visage", "Void Spirit",
    "Warlock", "Weaver", "Windranger", "Winter Wyvern", "Witch Doctor", "Wraith King",
    "Zeus"
]
