namespace SpriteKind {
    export const Boss1 = SpriteKind.create()
    export const ammo = SpriteKind.create()
    export const Boss2 = SpriteKind.create()
    export const tank = SpriteKind.create()
    export const tank2 = SpriteKind.create()
    export const boss2attack = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.tank, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    otherSprite.destroy(effects.spray, 100)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.stairWest, function (sprite6, location4) {
    game.splash("the door is locked ")
    tiles.placeOnTile(mySprite, tiles.getTileLocation(10, 7))
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`我的貼圖2`, function (sprite, location) {
    mySprite.sayText("!", 100, false)
    if (controller.A.isPressed()) {
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
        tiles.setTileAt(location, sprites.dungeon.floorLight2)
        machine_1 += 1
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`我的貼圖6`, function (sprite, location) {
    game.splash("thank for playing ch.2")
    info.setScore(8964)
    game.over(true, effects.smiles)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.isHittingTile(CollisionDirection.Bottom)) {
        mySprite.vy = -70
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.floorDarkDiamond, function (sprite, location) {
    mySprite.sayText("!", 100, false)
    if (controller.A.isPressed()) {
        game.splash("I am 江滭民")
        frog = sprites.create(img`
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
            `, SpriteKind.Boss2)
        frog.sayText("too young too simple")
        boss2_health += 70
        boss_fight2 += 1
        tiles.setTileAt(location, sprites.dungeon.floorDark2)
        info.setLife(5)
    }
})
sprites.onOverlap(SpriteKind.Boss2, SpriteKind.Projectile, function (sprite, otherSprite) {
    boss2_health += -1
    otherSprite.destroy(effects.rings, 500)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`我的貼圖8`, function (sprite12, location10) {
    tiles.setCurrentTilemap(tilemap`層級2`)
    tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 4))
    map2 += 1
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`我的貼圖4`, function (sprite, location) {
    if (bread != 3) {
        game.splash("is dog !!!!")
        tiles.placeOnTile(mySprite, tiles.getTileLocation(9, 12))
    }
    if (bread == 3) {
        game.splash("拿麵包", " 餵狗")
        tiles.setTileAt(location, sprites.dungeon.floorDark2)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.tank2, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    otherSprite.destroy(effects.spray, 100)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`我的貼圖7`, function (sprite8, location6) {
    map2 = 2
    tiles.setCurrentTilemap(tilemap`層級6`)
    tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 2))
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`我的貼圖3`, function (sprite, location) {
    mySprite.sayText("!", 100, false)
    if (controller.A.isPressed()) {
        if (bread != 2) {
            game.splash("i need 200kg麥子")
            tiles.placeOnTile(mySprite, tiles.getTileLocation(2, 9))
        }
        if (bread == 2) {
            game.splash("you make a bread")
            bread += 1
            tiles.setTileAt(location, sprites.dungeon.floorDark2)
        }
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleInsignia, function (sprite14, location12) {
    mySprite.sayText("!", 100, false)
    if (controller.A.isPressed()) {
        tiles.setTileAt(location12, sprites.dungeon.floorLight2)
        game.splash("吾名蔣介石!")
        mySprite2 = sprites.create(img`
            . . 4 4 4 4 4 . . 
            . 4 4 4 4 4 4 4 . 
            . 4 f 4 4 4 f 4 . 
            . 4 4 4 4 4 4 4 . 
            . 4 4 f f 4 4 4 . 
            . 4 4 4 4 4 4 4 . 
            . 4 f f f f 4 4 . 
            `, SpriteKind.Boss1)
        boss_fight1 += 1
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.boss2attack, function (sprite, otherSprite) {
    info.changeLifeBy(-1)
    otherSprite.destroy(effects.halo, 500)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleBlueCrystal, function (sprite, location) {
    mySprite.sayText("!", 100, false)
    if (controller.A.isPressed()) {
        game.splash("it transport to another place ")
        tiles.placeOnTile(mySprite, tiles.getTileLocation(12, 9))
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.chestClosed, function (sprite, location) {
    game.splash("you get 胡椒面")
    tiles.setTileAt(location, sprites.dungeon.floorDark2)
    attack += 1
    game.splash("down to shoot the ammo")
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`我的貼圖0`, function (sprite11, location9) {
    if (controller.A.isPressed()) {
        mySprite.vy = -70
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.purpleSwitchUp, function (sprite13, location11) {
    game.splash("the lava disappear")
    tiles.setTileAt(location11, sprites.dungeon.floorLight2)
    tiles.setTileAt(tiles.getTileLocation(10, 10), sprites.dungeon.floorLight2)
    tiles.setTileAt(tiles.getTileLocation(11, 10), sprites.dungeon.floorLight2)
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(img`
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
        `, mySprite, 0, -56)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.ammo, function (sprite2, otherSprite) {
    otherSprite.destroy(effects.coolRadial, 500)
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Boss1, function (sprite5, otherSprite2) {
    sprite5.destroy(effects.rings, 500)
    boss_health += -1
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`我的貼圖1`, function (sprite7, location5) {
    mySprite.sayText("!", 100, false)
    if (controller.A.isPressed()) {
        if (machine_1 == 0) {
            game.splash("I am mao zedong")
            game.splash("我要沼氣")
            game.splash("給我的話我給你開門")
            tiles.placeOnTile(mySprite, tiles.getTileLocation(9, 10))
        }
        if (machine_1 == 1) {
            game.splash("thank you ")
            game.splash("I love china")
            tiles.setTileAt(location5, sprites.dungeon.floorLight2)
            tiles.setTileAt(tiles.getTileLocation(7, 6), sprites.dungeon.floorLight2)
            tiles.setTileAt(tiles.getTileLocation(7, 7), sprites.dungeon.floorLight2)
            game.splash("fix the machine")
        }
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`我的貼圖9`, function (sprite9, location7) {
    game.splash("the door is locked")
    tiles.placeOnTile(mySprite, tiles.getTileLocation(5, 19))
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.greenSwitchUp, function (sprite3, location2) {
    game.splash("the door opens")
    tiles.setTileAt(location2, sprites.dungeon.floorLight2)
    tiles.setTileAt(tiles.getTileLocation(7, 3), sprites.dungeon.floorLight2)
    tiles.setTileAt(tiles.getTileLocation(7, 4), sprites.dungeon.floorLight2)
})
sprites.onOverlap(SpriteKind.tank, SpriteKind.Projectile, function (sprite, otherSprite) {
    otherSprite.destroy(effects.rings, 500)
    sprite.destroy(effects.rings, 500)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.stairEast, function (sprite10, location8) {
    game.splash("the door is locked ")
    tiles.placeOnTile(mySprite, tiles.getTileLocation(4, 18))
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`我的貼圖5`, function (sprite, location) {
    mySprite.sayText("!", 100, false)
    if (controller.A.isPressed()) {
        game.splash("you get 100kg麥子")
        bread += 1
        tiles.setTileAt(location, sprites.dungeon.floorDark2)
    }
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    if (attack == 1) {
        projectile = sprites.createProjectileFromSprite(img`
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
            `, mySprite, -60, 0)
        projectile = sprites.createProjectileFromSprite(img`
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
            `, mySprite, 60, 0)
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.collectibleRedCrystal, function (sprite, location) {
    mySprite.sayText("!", 100, false)
    if (controller.A.isPressed()) {
        game.splash("it transport to another place ")
        tiles.placeOnTile(mySprite, tiles.getTileLocation(14, 16))
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.greenSwitchDown, function (sprite9, location7) {
    game.splash("the lava disappear")
    tiles.setTileAt(location7, sprites.dungeon.floorLight2)
    tiles.setTileAt(tiles.getTileLocation(10, 13), sprites.dungeon.floorLight2)
    tiles.setTileAt(tiles.getTileLocation(11, 13), sprites.dungeon.floorLight2)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.stairSouth, function (sprite15, location13) {
    game.splash("the door is locked")
    tiles.placeOnTile(mySprite, tiles.getTileLocation(0, 4))
})
sprites.onOverlap(SpriteKind.tank2, SpriteKind.Projectile, function (sprite, otherSprite) {
    otherSprite.destroy(effects.rings, 500)
    sprite.destroy(effects.rings, 500)
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.hazardLava0, function (sprite4, location3) {
    mySprite.startEffect(effects.fire, 2000)
    info.changeLifeBy(-1)
    if (map2 == 0) {
        tiles.setTileAt(location3, sprites.castle.tileDarkGrass3)
    } else if (map2 == 1) {
        tiles.setTileAt(location3, sprites.dungeon.floorLight2)
    } else if (map2 == 2) {
        tiles.setTileAt(location3, sprites.dungeon.floorDark2)
    }
})
let tank1: Sprite = null
let tank2: Sprite = null
let projectile: Sprite = null
let attack = 0
let boss_fight1 = 0
let mySprite2: Sprite = null
let bread = 0
let frog: Sprite = null
let map2 = 0
let machine_1 = 0
let mySprite: Sprite = null
tiles.setCurrentTilemap(tilemap`層級1`)
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite, -70, 0)
controller.moveSprite(mySprite, 70, 0)
scene.cameraFollowSprite(mySprite)
info.setLife(2)
tiles.placeOnRandomTile(mySprite, sprites.builtin.forestTiles2)
machine_1 = 0
map2 = 0
let boss_health = 35
let boss_fight2 = 0
let boss2_health = 1
game.onUpdateInterval(2000, function () {
    if (boss_fight1 == 1) {
        tiles.placeOnTile(mySprite2, tiles.getTileLocation(randint(0, 5), 7))
    }
})
game.onUpdateInterval(2000, function () {
    if (boss_fight2 == 1) {
        tank2 = sprites.create(img`
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
            `, SpriteKind.tank)
        tank1 = sprites.create(img`
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
            `, SpriteKind.tank2)
        tiles.placeOnTile(tank1, tiles.getTileLocation(10, 19))
        tiles.placeOnTile(tank2, tiles.getTileLocation(0, 19))
        tank1.follow(mySprite, 70)
        tank2.follow(mySprite, 70)
    }
})
game.onUpdateInterval(2000, function () {
    if (boss_fight2 == 1) {
        tiles.placeOnTile(frog, tiles.getTileLocation(randint(4, 7), 15))
    }
})
forever(function () {
    mySprite.ay = 100
})
forever(function () {
    if (0 >= boss_health) {
        mySprite.sayText("I won", 2000, false)
        boss_fight1 = 2
        tiles.setTileAt(tiles.getTileLocation(7, 17), sprites.dungeon.floorLight2)
        tiles.setTileAt(tiles.getTileLocation(7, 18), sprites.dungeon.floorLight2)
        tiles.setTileAt(tiles.getTileLocation(0, 17), sprites.dungeon.floorLight2)
        tiles.setTileAt(tiles.getTileLocation(1, 17), sprites.dungeon.floorLight2)
        tiles.setTileAt(tiles.getTileLocation(2, 17), sprites.dungeon.floorLight2)
        tiles.setTileAt(tiles.getTileLocation(3, 17), sprites.dungeon.floorLight2)
        tiles.setTileAt(tiles.getTileLocation(4, 17), sprites.dungeon.floorLight2)
        tiles.setTileAt(tiles.getTileLocation(5, 17), sprites.dungeon.floorLight2)
        tiles.setTileAt(tiles.getTileLocation(6, 17), sprites.dungeon.floorLight2)
        tiles.setTileAt(tiles.getTileLocation(1, 18), sprites.dungeon.floorLight2)
        tiles.setTileAt(tiles.getTileLocation(2, 18), sprites.dungeon.floorLight2)
        tiles.setTileAt(tiles.getTileLocation(3, 18), sprites.dungeon.floorLight2)
        tiles.setTileAt(tiles.getTileLocation(4, 18), sprites.dungeon.floorLight2)
        tiles.setTileAt(tiles.getTileLocation(5, 18), sprites.dungeon.floorLight2)
        tiles.setTileAt(tiles.getTileLocation(6, 18), sprites.dungeon.floorLight2)
        boss_health = 1
        mySprite2.destroy(effects.spray, 500)
        tiles.setTileAt(tiles.getTileLocation(0, 18), sprites.dungeon.floorLight2)
    }
})
forever(function () {
    if (boss_fight1 == 1) {
        tiles.setTileAt(tiles.getTileLocation(0, 17), sprites.dungeon.hazardLava0)
        tiles.setTileAt(tiles.getTileLocation(1, 17), sprites.dungeon.hazardLava0)
        tiles.setTileAt(tiles.getTileLocation(2, 17), sprites.dungeon.hazardLava0)
        tiles.setTileAt(tiles.getTileLocation(3, 17), sprites.dungeon.hazardLava0)
        tiles.setTileAt(tiles.getTileLocation(5, 17), sprites.dungeon.hazardLava0)
        tiles.setTileAt(tiles.getTileLocation(6, 17), sprites.dungeon.hazardLava0)
        tiles.setTileAt(tiles.getTileLocation(0, 18), sprites.dungeon.hazardLava0)
        tiles.setTileAt(tiles.getTileLocation(1, 18), sprites.dungeon.hazardLava0)
        tiles.setTileAt(tiles.getTileLocation(2, 18), sprites.dungeon.hazardLava0)
        tiles.setTileAt(tiles.getTileLocation(3, 18), sprites.dungeon.hazardLava0)
        tiles.setTileAt(tiles.getTileLocation(4, 18), sprites.dungeon.hazardLava0)
        tiles.setTileAt(tiles.getTileLocation(5, 18), sprites.dungeon.hazardLava0)
        tiles.setTileAt(tiles.getTileLocation(6, 18), sprites.dungeon.hazardLava0)
    }
})
forever(function () {
    if (boss2_health <= 0) {
        mySprite.sayText("this guy is too young too simple", 4000, false)
        tiles.setTileAt(tiles.getTileLocation(11, 18), sprites.dungeon.floorDark2)
        tiles.setTileAt(tiles.getTileLocation(11, 19), sprites.dungeon.floorDark2)
        boss_fight2 = 2
        boss2_health += 1
        frog.destroy(effects.spray, 500)
    }
})
