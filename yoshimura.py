import discord
from discord.ext import commands
import random

# API info
characters = ["kaneki", "touka", "rize", "nishiki", "yoshimura", "tsukiyama", "hinami", "yomo", "uta", "itori", "jason", "ayato", "banjou", "nico", "eto", "kurona", "nashiro", "takizawa", "noro", "tatara", "amon", "mado", "hide", "juuzou", "yukinori", "akira", "arima", "urie", "shirazu", "tooru", "saiko", "sasaki", "ching-li", "touma"]
data_dict = {
    # ghouls
    "kaneki_name": "Ken Kaneki",
    "kaneki_textfield": "Su nombre se deriva del kanji dorado y del árbol (金木), que también son días de la semana jueves y viernes. (金曜日 / 木曜日). Tu apellido conocido (研) deriva de la palabra estudio, que indica tu intelecto. Kaneki tiene la costumbre de torcer la barbilla con la mano izquierda cada vez que miente o se siente incómodo, alejado de mamá.",
    "kaneki_image": "https://cdn.anisearch.com/images/character/cover/full/49/49893.jpg",
    "touka_name": "Touka Kirishima",
    "touka_textfield": "Sufre de ornitofobia (fobia a las aves), debido a un pájaro que le lastimó el ojo derecho (el ojo que cubre con su flequillo. A Touka le gusta la escuela y los conejos. Odia la literatura clásica, y en realidad quiere estudiar biología de Ghoul y don ' Montar un café como dice el anime.",
    "touka_image": "https://cdn.anisearch.com/images/character/cover/full/45/45987.jpg",
    "rize_name": "Rize Kamishiro",
    "rize_textfield": "Se destacaba por su capacidad de regeneración. Gracias a su Rinkaku Kagune podía curarse a sí misma, pero sólo con heridas no mortales. Si estaba malherida, o un órgano vital estaba dañado, podía recuperarse de ellas pero lentamente. Por esto, cuando tuvo su 'accidente' no pudo curarse a sí misma inmediatamente.",
    "rize_image": "https://cdn.anisearch.com/images/character/cover/full/45/45094.jpg",
    "nishiki_name": "Nishiki Nishio",
    "nishiki_textfield": "En su niñez sufrió carencias al lado de su hermana mayor que cuido de él, en su juventud perdió a su hermana a manos de investigadores por la traición de los humanos por ello su resentimiento a ellos hasta que conoce a Kimi una humana de la cual se enamora después de enfrentarse al gourmet se une al Anteiku y se vuelve cercano a Kaneki.",
    "nishiki_image": "https://cdn.anisearch.com/images/character/cover/full/46/46003.jpg",
    "yoshimura_name": "Kuzen Yoshimura",
    "yoshimura_textfield": "Tiene una similitud con Hinami, y es que ambos tenían problemas con el Kanji, en ambos casos una persona importante para ellos los ayudó con éste problema, Kaneki a Hinami y Ukina a Yoshimura y es de los pocos ghouls conocidos en ser de clase SSS, la más alta de todas.",
    "yoshimura_image": "https://cdn.anisearch.com/images/character/cover/full/43/43446.jpg",
    "tsukiyama_name": "Shuu Tsukiyama",
    "tsukiyama_textfield": "Estaba destinado a otro trabajo, hasta que el autor decidió agregarlo a Tokyo Ghoul. Hay varias especulaciones de que Tsukiyama es bisexual, hasta que se confirmó en una entrevista. Después de que Kaneki perdiera la memoria, Tsukiyama hizo una huelga de hambre durante 3 años.",
    "tsukiyama_image": "https://cdn.anisearch.com/images/character/cover/full/45/45986.jpg",
    "hinami_name": "Hinami Fueguchi",
    "hinami_textfield": "Los miembros de Aogiri se refieren a ella como Yotsume en referencia a la cresta japonesa, simboliza vigilancia, buena fortuna y protección de los malos espíritus, así como algo que parece débil pero posee una gran fuerza y heredó la mitad del kagune de su madre, dos alas en lugar de cuatro, pero heredó cuatro espinas en lugar de una del kagune de su padre.",
    "hinami_image": "https://cdn.anisearch.com/images/character/cover/full/43/43829.jpg",
    "yomo_name": "Renji Yomo",
    "yomo_textfield": "Hikari Kirishima, madre de Touka y Ayato, era hermana de Yomo Renji, por lo que Yomo es tio de Touka y Ayato. En el manga, un omake revela que él se emborracha fácilmente con el Vino de Sangre, y se vuelve estremadamente locuaz.",
    "yomo_image": "https://cdn.anisearch.com/images/character/cover/full/46/46465.jpg",
    "uta_name": "Uta",
    "uta_textfield": "Su nombre 'Uta' significa música y su tatuaje define la relación entre ghouls y humanos, además, su sentido del humor es algo extraño cuando le dio a Kaneki una máscara de Buda en el omake del volumen 2, leyó mal intencionadamente el nombre de Renji —particularmente el carácter Ji— como hemorroides",
    "uta_image": "https://cdn.anisearch.com/images/character/cover/full/45/45095.jpg",
    "itori_name": "Itori",
    "itori_textfield": "Es una vieja amiga de Yomo y Uta. Se le puede encontrar en el bar Helter Skelter, donde ella comparte y recolecta información sobre distintos asuntos. Pertenece al grupo de ghouls conocidos como los payaso.Tiene un lunar en el pecho izquierdo, un hecho que luego fue señalado por Sui Ishida.",
    "itori_image": "https://cdn.anisearch.com/images/character/cover/full/45/45096.jpg",
    "jason_name": "Yakumo Oomori",
    "jason_textfield": "Su apodo — Jason — es una referencia a Jason Voorhees, un personaje de las películas de Viernes 13, algo que también se ve referenciado en su distrito de origen, el Distrito 13. A veces, Yamori usa una máscara de hockey, la marca registrada de Jason Voorhees.",
    "jason_image": "https://cdn.anisearch.com/images/character/cover/full/46/46877.jpg",
    "ayato_name": "Ayato Kirishima",
    "ayato_textfield": "Él creció con su hermana en el Distrito 20 pero en algún punto del tiempo, abandonó el distrito. Ayato a estado por todos los distritos de Tokyo, trayendo consigo destrucción y caos sobre ellos, hasta que sus poderes y habilidades únicas fueron la atención de Tatara y, finalmente se unió al Árbol Aogiri, donde actualmente se desempeña como un alto oficial de la organización. Su apodo es 'Conejo negro' (ブラックラビット, Burakku Rabitto).",
    "ayato_image": "https://cdn.anisearch.com/images/character/cover/full/47/47074.jpg",
    "banjou_name": "Kazuichi Banjou",
    "banjou_textfield": "Es un exlíder de ghouls del distrito 11. Por lo general, se le ve con sus seguidores Ichimi, Jiro y Sante. Estaba enamorado de Rize Kamishiro. se considera el escudo de Kaneki y promete seguirlo a todas partes a las que este vaya y brindarle toda la ayuda posible.",
    "banjou_image": "https://cdn.anisearch.com/images/character/cover/full/45/45988.jpg",
    "nico_name": "Nico",
    "nico_textfield": "Le encantan los hombres buenos, las cosas bonitas, la diversión y los accesorios. Entre sus aficiones están el pulir su lado femenino, buscar un buen hombre, la moda y el canto. Él encuentra a hombres como Yamori, Ayato, Tatara, y Kaneki muy atractivos, aunque también vio hermosa a Touka Kirishima. Es el único personaje bisexual de la serie.",
    "nico_image": "https://cdn.anisearch.com/images/character/cover/full/46/46902.jpg",
    "eto_name": "Sen Takatsuki",
    "eto_textfield": "Es la hija de Yoshimura y su madre era una hermosa humana,por lo cual ella es un híbrido ghoul-humano. Es conocida también como el 'Búho', la líder del Aogiri. odia a su padre por abandonarla, dejarla a su suerte y no reclamarla (o eso piensa ella , ya que en realidad al ser una bebe fue arrebatada del lado de su progenitor).",
    "eto_image": "https://cdn.anisearch.com/images/character/cover/full/49/49312.jpg",
    "kurona_name": "Kurona Yasushisa",
    "kurona_textfield": "Según el Profesor Kanou, ella está considerado como un Floppy a pesar de no tener defectos inherentes. Desde de su aparición en la Isla Ru el color de su cabello es visto de color gris y es la única Ghoul de un Ojo capaz de presentar dos Kakugan en vez de uno, debido a su 'fusión' con su hermana.",
    "kurona_image": "https://cdn.anisearch.com/images/character/cover/full/49/49310.jpg",
    "nashiro_name": "Nashiro Yasushisa",
    "nashiro_textfield": "Según el Profesor Kanou, ella está considerado como un Floppy a pesar de no tener defectos inherentes. Su apodo concuerda con su color de cabello, al igual que el de su hermana Kurona. Es el único Ghoul de un ojo artificial cuyo Kakugan esta en su ojo derecho, el resto de los Ghoul artificiales tienen su Kakugan en su ojo Izquierdo. Es el segundo ghoul de un ojo conocido que posee su Kakugan en su ojo derecho, junto con Eto.",
    "nashiro_image": "https://cdn.anisearch.com/images/character/cover/full/49/49311.jpg",
    "takizawa_name": "Seidou Takizawa",
    "takizawa_textfield": "Cuando le recrimina a Ayato el tener preocupación por Hinami, considerando esto extraño ya que eran ghouls y le resultaba gracioso el ver como ghouls tenían sentimientos de preocupación por el otro, siendo estos monstruos. Demuestra que a pesar de ser un medio-ghoul todavía considera que los ghouls son monstruos.",
    "takizawa_image": "https://cdn.anisearch.com/images/character/cover/full/64/64067.jpg",
    "noro_name": "Noro",
    "noro_textfield": "Es posible que Noro haya pasado por el mismo proceso que Karren von Rosewald cuando Eto la torturó. Noro y Kanae exhibieron hazañas de regeneración similares, y sus kagune fueron similares en apariencia y función; también llevaban máscaras sorprendentemente similares.",
    "noro_image": "https://cdn.anisearch.com/images/character/cover/full/49/49787.jpg",
    "tatara_name": "Tatara",
    "tatara_textfield": "De acuerdo con el calendario de Tokyo Ghoul, tiene dificultades con la lectura del japonés y se queja de que le causa dolor de cabeza. Tatara considera a ghouls como Matasaka Kamishiro cobardes, y considera a cada miembro de Aogiri como 'Piezas de Repuesto'.",
    "tatara_image": "https://cdn.anisearch.com/images/character/cover/full/49/49791.jpg",
    
    # humanos
    "amon_name": "Koutarou Amon",
    "amon_textfield": "El investigador de CCG tiene el mismo nombre que el dios egipcio 'Amon Ra', que se traduce como 'Dios de todos los dioses'. El tatuaje en el cuello de Uta está escrito en griego y significa: 'No puedo vivir contigo o sin ti'. Uta fue violada por Mutsuki.",
    "amon_image": "https://cdn.anisearch.com/images/character/cover/full/43/43448.jpg",
    "mado_name": "Kureo Mado",
    "mado_textfield": "Mado amaba a su esposa e hija. También le gustan las armas que se obtuvieron a través del trabajo duro. Se revela que él tomó el apellido de su esposa al casarse con la familia Mado. Este agente del CCG tiene gran facilidad y motivación a la hora de combatir por ghouls, esto se debe a ciertos acontecimientos entre los ghouls y su familia.",
    "mado_image": "https://cdn.anisearch.com/images/character/cover/full/43/43828.jpg",
    "hide_name": "Hideyoshi Nagachika",
    "hide_textfield": "Es el mejor amigo de Kaneki desde que eran niños, se preocupa mucho por él y es muy optimista, tiene habilidades de observador y cuando descubre que su amigo es un monstruo en vez de alejarse (casi es devorado por Kaneki) lo encubre, aún que este último no se entere si no hasta el final de la historia de que su mejor amigo sabía la verdad sobre el. Es el hijo de un investigador del CCG que murió en una operación anti-ghoul",
    "hide_image": "https://cdn.anisearch.com/images/character/cover/full/43/43826.jpg",
    "juuzou_name": "Juuzou Suzuya",
    "juuzou_textfield": "No siente ningún dolor físico o emocional debido al sufrimiento infantil a manos de la Mujer Ghoul Big Mama. Por eso sigue cortando y cosiendo ella misma, para sentirse viva.",
    "juuzou_image": "https://cdn.anisearch.com/images/character/cover/full/49/49313.jpg",
    "yukinori_name": "Yukinori Shinohara",
    "yukinori_textfield": "Es un Investigador Ghoul de clase especial. En el pasado, se desempeñó como Instructor de Koutarou Amon en la Academia. Actualmente se encuentra asignado al distrito 20, y es responsable de la investigación del 'Glotón'. siente un gran cariño hacía Juuzou y lo ve por poco como si fuera un hijo, enseñándole todo lo posible y trata de cuidarlo en todo momento.",
    "yukinori_image": "https://cdn.anisearch.com/images/character/cover/full/46/46467.jpg","akira_name": "Akira Mado",
    "akira_textfield": "Es una investigadora ghoul de clase especial asociado. Es la hija de Kureo, y es una gran investigadora con un talento para la investigación junto a una gran inteligencia para la lucha, al igual que su padre está obsesionada con el Búho de un ojo y busca encontrarlo para poder vengarse de este, su compañero es Amon y con el tiempo comienza a desarrollar una atracción a este como algo más que su superior, siendo que en un principio lo subestimaba y no confiaba mucho en este además de guardarle un poco de rencor. Akira ha demostrado el mismo ojo abierto y el otro entrecerrado como su padre durante la Operación de Limpieza de la Subasta, mientras se enfrentaba a Naki.",
    "akira_image": "https://cdn.anisearch.com/images/character/cover/full/49/49314.jpg",
    "arima_name": "Kishou Arima",
    "arima_textfield": "Es un investigador de clase especial. Es el mejor investigador de toda la historia, le conocen como el investigador más fuerte y según los mismos ghouls él es su shinigami (dios de la muerte según la cultura japonesa), con tan solo 16 años ya hacía misiones para el CCG y se le atribuye un talento excepcional, siempre que existe un ghoul difícil de exterminar le asignan a este el caso. en Tokyo Ghoul: Jack, hablan un poco sobre su pasado.",
    "arima_image": "https://cdn.anisearch.com/images/character/cover/full/52/52902.jpg",

    # quinx
    "urie_name": "Kuki Urie",
    "urie_textfield": "Anteriormente, tuvo un nivel factorial de Rc de 902, el segundo más alto en comparación con los otros miembros del Escuadrón Quinx original. En la actualidad, su nivel es de 1911, el cual sobrepasa los límites de la diferencia entre los humanos y los ghouls, por lo tanto, sus consecuencias serán los síntomas de un ghoul y la pérdida de control de su kagune.",
    "urie_image": "https://cdn.anisearch.com/images/character/cover/full/63/63116.jpg",
    "shirazu_name": "Gishi Shirazu",
    "shirazu_textfield": "Shirazu tenía un factor de Rc nivel 920. El más alto del Escuadrón Quinx original. Shirazu estaba enamorado de su superior Akira Mado, y se refiere a ella como la 'Santa Madre' del CCG. Su equipo parece ser consciente de este hecho.",
    "shirazu_image": "https://cdn.anisearch.com/images/character/cover/full/63/63309.jpg",
    "tooru_name": "Tooru Mutsuki",
    "tooru_textfield": "Mutsuki tiene numerosos rasgos en común con el Kaneki del comienzo de la serie original, incluyendo su personalidad amable y dificultad para controlar sus poderes. Los dos comparten aún mayores rasgos derivados de su pasado por ciertos eventos. Es el primer personaje transgénero de la serie",
    "tooru_image": "https://cdn.anisearch.com/images/character/cover/full/63/63234.jpg",
    "saiko_name": "Saiko Yonebayashi",
    "saiko_textfield": "No le gusta tener que trabajar, ella prefiere tener una vida feliz, despreocupada y relajada. Es tranquila al jugar videojuegos y comer comida chatarra en exceso. A menudo se queda dormida, que le gana la ausencia de la mayoría de las misiones.",
    "saiko_image": "https://cdn.anisearch.com/images/character/cover/full/63/63310.jpg",
    "sasaki_name": "Sasaki Haise",
    "sasaki_textfield": "Es una de las muchas personalidades que Kaneki a obtenido a lo largo del manga. En el pasado, Haise era conocido Ojo Parcheado, y era considerado un ghoul de rango SS. Sasaki solía llevar una chaqueta de color blanca, similar a la que suelen llevar los demás inspectores Ghouls de la central.",
    "sasaki_image": "https://cdn.anisearch.com/images/character/cover/full/63/63235.jpg",
    "ching-li_name": "Ching-Li Hsiao",
    "ching-li_textfield": "Es una Pacificadora y una miembro del segundo grupo de reclutas del Escuadrón Quinx originaria de Taiwán. Estuvo entre los estudiantes superdotados en el Jardín del Sol Blanco y está especializada en el combate a mano.",
    "ching-li_image": "https://cdn.anisearch.com/images/character/cover/full/81/81766.jpg", 
    "touma_name": "Touma Higemaru",
    "touma_textfield": "Touma Higemaru es un Pacificador y uno de los miembros del segundo grupo de reclutas del Escuadrón Quinx. Proviene de una familia rica y de gente bien posicionada, especializada en Protección Civil como la Policía y los Bomberos. Usa guantes al igual que su líder de escuadrón",
    "touma_image": "https://cdn.anisearch.com/images/character/cover/full/82/82038.jpg",  
}
# bot commands
bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    game = discord.Game('Anteiku')
    await bot.change_presence(status=discord.Status.idle, activity=game)

@bot.command()
async def data(ctx, character=None):
    if character==None:
        random_character = random.choice(characters)
        embed = discord.Embed(title=data_dict["%s_name"% random_character], description= data_dict["%s_textfield"% random_character], color=discord.Color.red())
        embed.set_thumbnail(url=data_dict["%s_image"% random_character])
        await ctx.send(embed=embed)
        del random_character

    elif character=="all":
        for i in characters:
            embed = discord.Embed(title=data_dict["%s_name"% i], description= data_dict["%s_textfield"% i], color=discord.Color.red())
            embed.set_thumbnail(url=data_dict["%s_image"% i])
            await ctx.send(embed=embed)

    else:
        try:
            embed = discord.Embed(title=data_dict["%s_name"% character], description= data_dict["%s_textfield"% character], color=discord.Color.red())
            embed.set_thumbnail(url=data_dict["%s_image"% character])
            await ctx.send(embed=embed)
        
        except:
            await ctx.send("No se encontró el personaje")

@bot.command()
async def list(ctx):
    embed = discord.Embed(title="Lista de personajes disponibles", description="")
    for i in characters:
        embed.description += ">data %s \n"% i
    await ctx.send(embed=embed)


@bot.command()
async def curio(ctx):
    random_curiosity = random.choice(curiosities)
    embed = discord.Embed(title=random_curiosity, description= curiosities[random_curiosity], color=discord.Color.red())
    embed.set_thumbnail(url=data_dict["%s_image"% random_curiosity])
    await ctx.send(embed=embed)
    del random_curiosity

bot.run('ODEwOTA3MTM2MDkwODMyOTc5.YCqeHw.gHSsA4qFek8e58Uu6RSp_3tr6vE')
