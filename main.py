@namespace
class SpriteKind:
    Boss1 = SpriteKind.create()
    ammo = SpriteKind.create()
    Boss2 = SpriteKind.create()
    tank = SpriteKind.create()
    tank2 = SpriteKind.create()
    boss2attack = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    info.change_life_by(-1)
    otherSprite.destroy(effects.spray, 100)
sprites.on_overlap(SpriteKind.player, SpriteKind.tank, on_on_overlap)

def on_overlap_tile(sprite6, location4):
    game.splash("the door is locked ")
    tiles.place_on_tile(mySprite, tiles.get_tile_location(10, 7))
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_west,
    on_overlap_tile)

def on_overlap_tile2(sprite2, location):
    global machine_1
    mySprite.say_text("!", 100, False)
    if controller.A.is_pressed():
        game.splash("有一點難打開")
        game.splash("用力中")
        game.splash("1")
        game.splash("2")
        game.splash("3")
        game.splash("4")
        game.splash("5")
        game.splash("6")
        game.splash("7")
        game.splash("8964")
        game.splash("滿臉噴$了cao")
        tiles.set_tile_at(location, sprites.dungeon.floor_light2)
        machine_1 += 1
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        我的貼圖2
    """),
    on_overlap_tile2)

def on_a_pressed():
    if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite.vy = -70
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile3(sprite3, location2):
    global mySprite3, boss2_health, boss_fight2
    game.splash("I am 江滭民")
    mySprite3 = sprites.create(img("""
            . . . . . . . . . . . . . . 7 . 
                    7 . . . . . . . . . . . . 7 7 . 
                    . 7 6 6 6 6 6 6 6 6 6 6 6 7 . . 
                    . 7 6 6 6 6 6 6 6 6 6 6 7 7 . . 
                    . 7 7 6 6 6 6 6 6 6 6 7 7 . . . 
                    . . 7 6 6 6 6 6 6 6 6 7 6 . . . 
                    . . 6 6 6 6 6 6 6 6 6 6 6 . . . 
                    . . 6 6 6 6 6 6 6 6 6 6 6 . . . 
                    . . 7 6 6 6 6 6 6 6 6 6 7 7 . . 
                    . 7 7 7 7 7 7 7 7 7 7 7 7 7 . . 
                    . 7 7 1 1 7 7 7 7 1 1 7 7 7 . . 
                    7 . 7 1 f 7 7 7 7 f 1 7 7 7 7 . 
                    7 . 7 7 7 7 7 7 7 7 7 7 7 . 7 . 
                    7 . 7 7 7 7 2 2 7 7 7 7 7 . 7 . 
                    7 . . . . . 2 2 . . . . . . 7 . 
                    . . . . . . 2 2 . . . . . . . .
        """),
        SpriteKind.Boss2)
    mySprite3.say_text("too young too simple")
    boss2_health += 50
    boss_fight2 += 1
    tiles.set_tile_at(location2, sprites.dungeon.floor_dark2)
    info.set_life(10)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.floor_dark_diamond,
    on_overlap_tile3)

def on_on_overlap2(sprite4, otherSprite2):
    global boss2_health
    boss2_health += -1
    otherSprite2.destroy(effects.rings, 500)
sprites.on_overlap(SpriteKind.Boss2, SpriteKind.projectile, on_on_overlap2)

def on_overlap_tile4(sprite5, location3):
    if bread != 3:
        game.splash("is dog !!!!")
        tiles.place_on_tile(mySprite, tiles.get_tile_location(9, 12))
    if bread == 3:
        game.splash("拿麵包餵狗")
        tiles.set_tile_at(location3, sprites.dungeon.floor_dark2)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        我的貼圖4
    """),
    on_overlap_tile4)

def on_on_overlap3(sprite7, otherSprite3):
    info.change_life_by(-1)
    otherSprite3.destroy(effects.spray, 100)
sprites.on_overlap(SpriteKind.player, SpriteKind.tank2, on_on_overlap3)

def on_overlap_tile5(sprite8, location5):
    global bread
    mySprite.say_text("!", 100, False)
    if controller.A.is_pressed():
        if bread != 2:
            game.splash("i need 200kg麥子")
            tiles.place_on_tile(mySprite, tiles.get_tile_location(2, 9))
        if bread == 2:
            game.splash("you make a bread")
            bread += 1
            tiles.set_tile_at(location5, sprites.dungeon.floor_dark2)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        我的貼圖3
    """),
    on_overlap_tile5)

def on_overlap_tile6(sprite14, location12):
    global mySprite2, boss_fight1
    mySprite.say_text("!", 100, False)
    if controller.A.is_pressed():
        tiles.set_tile_at(location12, sprites.dungeon.floor_light2)
        game.splash("吾名蔣介石!")
        mySprite2 = sprites.create(img("""
                . . 4 4 4 4 4 . . 
                            . 4 4 4 4 4 4 4 . 
                            . 4 f 4 4 4 f 4 . 
                            . 4 4 4 4 4 4 4 . 
                            . 4 4 f f 4 4 4 . 
                            . 4 4 4 4 4 4 4 . 
                            . 4 f f f f 4 4 .
            """),
            SpriteKind.Boss1)
        tiles.place_on_tile(mySprite2, tiles.get_tile_location(3, 13))
        boss_fight1 += 1
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_insignia,
    on_overlap_tile6)

def on_on_overlap4(sprite9, otherSprite4):
    info.change_life_by(-1)
    otherSprite4.destroy(effects.halo, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.boss2attack, on_on_overlap4)

def on_overlap_tile7(sprite10, location6):
    mySprite.say_text("!", 100, False)
    if controller.A.is_pressed():
        game.splash("it transport to another place ")
        tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_red_crystal)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_blue_crystal,
    on_overlap_tile7)

def on_overlap_tile8(sprite11, location7):
    global attack
    game.splash("you get 胡椒面")
    tiles.set_tile_at(location7, sprites.dungeon.floor_dark2)
    attack += 1
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile8)

def on_overlap_tile9(sprite112, location9):
    if controller.A.is_pressed():
        mySprite.vy = -70
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        我的貼圖0
    """),
    on_overlap_tile9)

def on_overlap_tile10(sprite13, location11):
    game.splash("the lava disappear")
    tiles.set_tile_at(location11, sprites.dungeon.floor_light2)
    tiles.set_tile_at(tiles.get_tile_location(10, 10),
        sprites.dungeon.floor_light2)
    tiles.set_tile_at(tiles.get_tile_location(11, 10),
        sprites.dungeon.floor_light2)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.purple_switch_up,
    on_overlap_tile10)

def on_overlap_tile11(sprite82, location62):
    global map2
    map2 = 2
    tiles.set_current_tilemap(tilemap("""
        層級6
    """))
    tiles.place_on_tile(mySprite, tiles.get_tile_location(0, 2))
scene.on_overlap_tile(SpriteKind.player,
    sprites.swamp.swamp_tile13,
    on_overlap_tile11)

def on_b_pressed():
    global projectile
    if attack == 0:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            5 . . . . . . . . . . . . . . . 
                            . 5 . . . . . . . . . . . . . 5 
                            . 5 5 . . . . e . . . . 5 5 5 5 
                            . . 5 5 . . e e e . . . 5 . . . 
                            . . . . . e e e e e . . . . . . 
                            . . . . e e e e e e e . . . . . 
                            . . . e e e e e e e e e . . . . 
                            . . e e e e e e e e e e e . . . 
                            . . e e e e e e e e e e e . . . 
                            . . e e e e e e e e e e e . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            0,
            -56)
    if attack == 1:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            5 . . . . . . . . . . . . . . . 
                            . 5 . . . . . . . . . . . . . 5 
                            . 5 5 . . . . e . . . . 5 5 5 5 
                            . . 5 5 . . e e e . . . 5 . . . 
                            . . . . . e e e e e . . . . . . 
                            . . . . e e e e e e e . . . . . 
                            . . . e e e e e e e e e . . . . 
                            . . e e e e e e e e e e e . . . 
                            . . e e e e e e e e e e e . . . 
                            . . e e e e e e e e e e e . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            0,
            -56)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . 2 2 2 2 2 2 2 2 2 2 2 . . 
                            . . . 2 4 4 4 5 4 4 4 4 4 2 . . 
                            . . . 2 4 4 5 5 5 5 5 5 4 2 . . 
                            . . . 2 5 5 5 5 4 4 5 5 4 2 . . 
                            . . . 2 4 4 5 5 4 5 5 5 4 2 . . 
                            . . . 2 4 4 5 4 5 5 5 4 4 2 . . 
                            . . . 2 5 5 5 5 5 5 5 4 4 2 . . 
                            . . . 2 4 4 5 5 5 4 5 5 4 2 . . 
                            . . . 2 4 5 5 4 4 4 4 4 4 2 . . 
                            . . . 2 2 2 2 2 2 2 2 2 2 2 . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            -60,
            0)
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . 2 2 2 2 2 2 2 2 2 2 2 . . 
                            . . . 2 4 4 4 5 4 4 4 4 4 2 . . 
                            . . . 2 4 4 5 5 5 5 5 5 4 2 . . 
                            . . . 2 5 5 5 5 4 4 5 5 4 2 . . 
                            . . . 2 4 4 5 5 4 5 5 5 4 2 . . 
                            . . . 2 4 4 5 4 5 5 5 4 4 2 . . 
                            . . . 2 5 5 5 5 5 5 5 4 4 2 . . 
                            . . . 2 4 4 5 5 5 4 5 5 4 2 . . 
                            . . . 2 4 5 5 4 4 4 4 4 4 2 . . 
                            . . . 2 2 2 2 2 2 2 2 2 2 2 . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            60,
            0)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_on_overlap5(sprite22, otherSprite5):
    otherSprite5.destroy(effects.cool_radial, 500)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.ammo, on_on_overlap5)

def on_on_overlap6(sprite52, otherSprite22):
    global boss_health
    sprite52.destroy(effects.rings, 500)
    boss_health += -1
sprites.on_overlap(SpriteKind.projectile, SpriteKind.Boss1, on_on_overlap6)

def on_overlap_tile12(sprite72, location52):
    mySprite.say_text("!", 100, False)
    game.splash("I am mao zedong")
    if controller.A.is_pressed():
        if machine_1 == 0:
            game.splash("我要沼氣")
            game.splash("給我的話我給你開門")
            tiles.place_on_tile(mySprite, tiles.get_tile_location(9, 10))
        if machine_1 == 1:
            game.splash("thank you ")
            game.splash("I love china")
            tiles.set_tile_at(location52, sprites.dungeon.floor_light2)
            tiles.set_tile_at(tiles.get_tile_location(7, 6), sprites.dungeon.floor_light2)
            tiles.set_tile_at(tiles.get_tile_location(7, 7), sprites.dungeon.floor_light2)
            game.splash("fix the machine")
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        我的貼圖1
    """),
    on_overlap_tile12)

def on_overlap_tile13(sprite32, location22):
    game.splash("the door opens")
    tiles.set_tile_at(location22, sprites.dungeon.floor_light2)
    tiles.set_tile_at(tiles.get_tile_location(7, 3), sprites.dungeon.floor_light2)
    tiles.set_tile_at(tiles.get_tile_location(7, 4), sprites.dungeon.floor_light2)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.green_switch_up,
    on_overlap_tile13)

def on_on_overlap7(sprite12, otherSprite6):
    otherSprite6.destroy(effects.rings, 500)
    sprite12.destroy(effects.rings, 500)
sprites.on_overlap(SpriteKind.tank, SpriteKind.projectile, on_on_overlap7)

def on_overlap_tile14(sprite122, location10):
    global map2
    tiles.set_current_tilemap(tilemap("""
        層級2
    """))
    tiles.place_on_tile(mySprite, tiles.get_tile_location(0, 4))
    map2 += 1
scene.on_overlap_tile(SpriteKind.player,
    sprites.castle.tile_grass2,
    on_overlap_tile14)

def on_overlap_tile15(sprite102, location8):
    game.splash("the door is locked ")
    tiles.place_on_tile(mySprite, tiles.get_tile_location(4, 18))
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_east,
    on_overlap_tile15)

def on_overlap_tile16(sprite15, location13):
    global bread
    mySprite.say_text("!", 100, False)
    if controller.A.is_pressed():
        game.splash("you get 100kg麥子")
        bread += 1
        tiles.set_tile_at(location13, sprites.dungeon.floor_dark2)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        我的貼圖5
    """),
    on_overlap_tile16)

def on_overlap_tile17(sprite16, location14):
    mySprite.say_text("!", 100, False)
    if controller.A.is_pressed():
        game.splash("it transport to another place ")
        tiles.place_on_random_tile(mySprite, sprites.dungeon.collectible_blue_crystal)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.collectible_red_crystal,
    on_overlap_tile17)

def on_overlap_tile18(sprite92, location72):
    game.splash("the lava disappear")
    tiles.set_tile_at(location72, sprites.dungeon.floor_light2)
    tiles.set_tile_at(tiles.get_tile_location(10, 13),
        sprites.dungeon.floor_light2)
    tiles.set_tile_at(tiles.get_tile_location(11, 13),
        sprites.dungeon.floor_light2)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.green_switch_down,
    on_overlap_tile18)

def on_overlap_tile19(sprite152, location132):
    game.splash("the door is locked")
    tiles.place_on_tile(mySprite, tiles.get_tile_location(0, 4))
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.stair_south,
    on_overlap_tile19)

def on_on_overlap8(sprite17, otherSprite7):
    otherSprite7.destroy(effects.rings, 500)
    sprite17.destroy(effects.rings, 500)
sprites.on_overlap(SpriteKind.tank2, SpriteKind.projectile, on_on_overlap8)

def on_overlap_tile20(sprite18, location15):
    mySprite4.destroy(effects.warm_radial, 500)
scene.on_overlap_tile(SpriteKind.boss2attack,
    sprites.dungeon.floor_mixed,
    on_overlap_tile20)

def on_overlap_tile21(sprite42, location32):
    mySprite.start_effect(effects.fire, 2000)
    info.change_life_by(-1)
    if map2 == 0:
        tiles.set_tile_at(location32, sprites.castle.tile_dark_grass3)
    elif map2 == 1:
        tiles.set_tile_at(location32, sprites.dungeon.floor_light2)
    elif map2 == 2:
        tiles.set_tile_at(location32, sprites.dungeon.floor_dark2)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.hazard_lava0,
    on_overlap_tile21)

tank1: Sprite = None
tank22: Sprite = None
mySprite4: Sprite = None
projectile: Sprite = None
attack = 0
boss_fight1 = 0
mySprite2: Sprite = None
bread = 0
boss2_health = 0
mySprite3: Sprite = None
map2 = 0
machine_1 = 0
mySprite: Sprite = None
tiles.set_current_tilemap(tilemap("""
    層級1
"""))
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . 5 5 5 . . . . . . 5 5 5 . . 
            . . 5 5 5 . . . . . . 5 5 5 . . 
            . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
            . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
            . . 5 5 f 5 5 5 5 5 5 f 5 5 . . 
            . . 5 5 f 5 5 5 5 5 5 f 5 5 . . 
            . . 5 5 5 5 5 f f 5 5 5 5 5 . . 
            . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
            . . 5 f 5 5 5 5 5 5 5 f 5 5 . . 
            . . 5 5 f f f f f f f 5 5 5 . . 
            . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
            . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
            . . 5 5 5 5 5 5 5 5 5 5 5 5 . . 
            . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
            . . 2 2 2 2 2 2 2 2 2 2 2 2 . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, -70, 0)
controller.move_sprite(mySprite, 70, 0)
scene.camera_follow_sprite(mySprite)
info.set_life(2)
tiles.place_on_random_tile(mySprite, sprites.builtin.forest_tiles2)
machine_1 = 0
map2 = 0
boss_health = 35
boss_fight2 = 0

def on_update_interval():
    if boss_fight2 == 1:
        tiles.place_on_tile(mySprite3, tiles.get_tile_location(randint(4, 7), 16))
game.on_update_interval(5000, on_update_interval)

def on_update_interval2():
    if boss_fight1 == 1:
        tiles.place_on_tile(mySprite2, tiles.get_tile_location(randint(0, 5), 7))
game.on_update_interval(2000, on_update_interval2)

def on_update_interval3():
    global tank22, tank1
    if boss_fight2 == 1:
        tank22 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . 5 5 5 5 5 . . . . . 
                            . . . . . . 5 5 5 5 5 . . . . . 
                            . . . . . . 5 5 5 5 5 . . . . . 
                            . . . 7 7 7 7 7 7 7 7 7 7 7 . . 
                            5 5 5 7 7 7 7 7 7 7 7 7 7 7 . . 
                            5 5 5 7 7 7 7 7 7 7 7 7 7 7 . . 
                            . . . 7 7 7 7 7 7 7 7 7 7 7 . . 
                            . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . 
                            . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . 
                            . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . 
                            . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                            . 8 f f f f f f f f f f f f 8 . 
                            . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.tank)
        tank1 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . 5 5 5 5 5 . . . . . . 
                            . . . . . 5 5 5 5 5 . . . . . . 
                            . . . . . 5 5 5 5 5 . . . . . . 
                            . . 7 7 7 7 7 7 7 7 7 7 7 . . . 
                            . . 7 7 7 7 7 7 7 7 7 7 7 5 5 5 
                            . . 7 7 7 7 7 7 7 7 7 7 7 5 5 5 
                            . . 7 7 7 7 7 7 7 7 7 7 7 . . . 
                            . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . 
                            . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . 
                            . 7 7 7 7 7 7 7 7 7 7 7 7 7 7 . 
                            . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                            . 8 f f f f f f f f f f f f 8 . 
                            . 8 8 8 8 8 8 8 8 8 8 8 8 8 8 . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.tank2)
        tiles.place_on_tile(tank1, tiles.get_tile_location(10, 19))
        tiles.place_on_tile(tank22, tiles.get_tile_location(0, 19))
        tank1.follow(mySprite, 70)
        tank22.follow(mySprite, 70)
game.on_update_interval(2000, on_update_interval3)

def on_update_interval4():
    global mySprite4
    if boss_fight2 == 1:
        mySprite4 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . 2 2 2 2 2 2 2 2 2 . . . 
                            . . . . 2 7 7 7 7 7 7 7 2 . . . 
                            . . . . 2 7 7 7 7 7 7 7 2 . . . 
                            . . . . 2 7 7 5 5 5 7 7 2 . . . 
                            . . . . 2 7 7 5 5 5 7 7 2 . . . 
                            . . . . 2 7 7 5 5 5 7 7 2 . . . 
                            . . . . 2 7 7 5 5 5 7 7 2 . . . 
                            . . . . 2 7 7 7 7 7 7 7 2 . . . 
                            . . . . 2 7 7 7 7 7 7 7 2 . . . 
                            . . . . 2 2 2 2 2 2 2 2 2 . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.boss2attack)
        tiles.place_on_tile(mySprite4, tiles.get_tile_location(randint(4, 7), 16))
        mySprite4.set_velocity(0, -50)
        mySprite4.set_bounce_on_wall(False)
game.on_update_interval(2000, on_update_interval4)

def on_forever():
    mySprite.ay = 100
forever(on_forever)

def on_forever2():
    global boss_fight1, boss_health
    if 0 >= boss_health:
        mySprite.say_text("I won", 2000, False)
        boss_fight1 = 2
        tiles.set_tile_at(tiles.get_tile_location(7, 17), sprites.dungeon.floor_light2)
        tiles.set_tile_at(tiles.get_tile_location(7, 18), sprites.dungeon.floor_light2)
        tiles.set_tile_at(tiles.get_tile_location(0, 17), sprites.dungeon.floor_light2)
        tiles.set_tile_at(tiles.get_tile_location(1, 17), sprites.dungeon.floor_light2)
        tiles.set_tile_at(tiles.get_tile_location(2, 17), sprites.dungeon.floor_light2)
        tiles.set_tile_at(tiles.get_tile_location(3, 17), sprites.dungeon.floor_light2)
        tiles.set_tile_at(tiles.get_tile_location(4, 17), sprites.dungeon.floor_light2)
        tiles.set_tile_at(tiles.get_tile_location(5, 17), sprites.dungeon.floor_light2)
        tiles.set_tile_at(tiles.get_tile_location(6, 17), sprites.dungeon.floor_light2)
        tiles.set_tile_at(tiles.get_tile_location(0, 18), sprites.dungeon.floor_light2)
        tiles.set_tile_at(tiles.get_tile_location(1, 18), sprites.dungeon.floor_light2)
        tiles.set_tile_at(tiles.get_tile_location(2, 18), sprites.dungeon.floor_light2)
        tiles.set_tile_at(tiles.get_tile_location(3, 18), sprites.dungeon.floor_light2)
        tiles.set_tile_at(tiles.get_tile_location(4, 18), sprites.dungeon.floor_light2)
        tiles.set_tile_at(tiles.get_tile_location(5, 18), sprites.dungeon.floor_light2)
        tiles.set_tile_at(tiles.get_tile_location(6, 18), sprites.dungeon.floor_light2)
        boss_health = 1
        mySprite2.destroy(effects.spray, 500)
forever(on_forever2)

def on_forever3():
    if boss_fight1 == 1:
        tiles.set_tile_at(tiles.get_tile_location(0, 17), sprites.dungeon.hazard_lava0)
        tiles.set_tile_at(tiles.get_tile_location(1, 17), sprites.dungeon.hazard_lava0)
        tiles.set_tile_at(tiles.get_tile_location(2, 17), sprites.dungeon.hazard_lava0)
        tiles.set_tile_at(tiles.get_tile_location(3, 17), sprites.dungeon.hazard_lava0)
        tiles.set_tile_at(tiles.get_tile_location(4, 17), sprites.dungeon.hazard_lava0)
        tiles.set_tile_at(tiles.get_tile_location(5, 17), sprites.dungeon.hazard_lava0)
        tiles.set_tile_at(tiles.get_tile_location(6, 17), sprites.dungeon.hazard_lava0)
        tiles.set_tile_at(tiles.get_tile_location(0, 18), sprites.dungeon.hazard_lava0)
        tiles.set_tile_at(tiles.get_tile_location(1, 18), sprites.dungeon.hazard_lava0)
        tiles.set_tile_at(tiles.get_tile_location(2, 18), sprites.dungeon.hazard_lava0)
        tiles.set_tile_at(tiles.get_tile_location(3, 18), sprites.dungeon.hazard_lava0)
        tiles.set_tile_at(tiles.get_tile_location(4, 18), sprites.dungeon.hazard_lava0)
        tiles.set_tile_at(tiles.get_tile_location(5, 18), sprites.dungeon.hazard_lava0)
        tiles.set_tile_at(tiles.get_tile_location(6, 18), sprites.dungeon.hazard_lava0)
forever(on_forever3)

def on_forever4():
    global boss_fight2, boss2_health
    if boss2_health <= 0:
        mySprite.say_text("this guy is too young too simple", 500, False)
        tiles.set_tile_at(tiles.get_tile_location(11, 18), sprites.dungeon.floor_dark2)
        tiles.set_tile_at(tiles.get_tile_location(11, 19), sprites.dungeon.floor_dark2)
        boss_fight2 = 2
        mySprite3.destroy()
        boss2_health += 1
forever(on_forever4)
