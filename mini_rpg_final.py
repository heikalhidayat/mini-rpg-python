#import library yang dibutuhkan
import random
import time

## Informasi Hero
# knight memiliki komposisi kekuatan yang merata pada semua aspek
knight_exp = 0
knight_level = 0
knight_hp = 100
knight_attack = 15
knight_agility = 15
knight_defense = 15

# Assasin memiliki agility yang tinggi tapi rendah dalam atack dan defense
assasin_exp = 0
assasin_level = 0
assasin_hp = 100
assasin_attack = 10
assasin_agility = 25
assasin_defense = 8

# Mage memiliki serangan yang sangat kuat tapi sangat rendah dalam agility dan defense
mage_exp = 0
mage_level = 0
mage_hp = 100
mage_attack = 30
mage_agility = 8
mage_defense = 8

## Informasi Monster
monster_exp = 50
monster_level = 0
monster_hp = 10
monster_attack = 10
monster_agility = 10
monster_defense = 10

monster2_exp = 100
mosnter2_level = 0
monster2_hp = 10
monster2_attack = 20
monster2_agility = 15
monster2_defense = 20

monster3_exp = 75
monster3_level = 0
monster3_hp = 10
monster3_attack = 10
monster3_agility = 20
monster3_defense = 15

# Daftar Item - item dapat memberikan pahlawan tambahan ability
pedang_tajam = 10
perisai_kayu = 5
perisai_besi = 10
sepatu_sihir = 10
ramuan_penyembuh = 10
drop_item = ["pedang_tajam", "perisai_kayu", "perisai_besi", "sepatu_sihir", "ramuan_penyembuh"]

## Informasi Karakter
# Nama Hero
daftar_karakter = {
    "kall": {
        "hp": knight_hp,
        "attack": knight_attack,
        "agility": knight_agility,
        "defense": knight_defense
    },
    "karu": {
        "hp": assasin_hp,
        "attack": assasin_attack,
        "agility": assasin_agility,
        "defense": assasin_defense
    },
    "celsy": {
        "hp": mage_hp,
        "attack": mage_attack,
        "agility": mage_agility,
        "defense": mage_defense
    },
    "goblin": {
        "hp": monster_hp,
        "attack": monster_attack,
        "agility": monster_agility,
        "defense": monster_defense
    },
    "orc": {
        "hp": monster2_hp,
        "attack": monster2_attack,
        "agility": monster2_agility,
        "defense": monster2_defense
    },
    "lizard": {
        "hp": monster3_hp,
        "attack": monster3_attack,
        "agility": monster3_agility,
        "defense": monster3_defense
    }
}

# hero Player

print("kall")
print("karu")
print("celsy")
player = input("Pilih Hero Anda!! ").lower()

if player in daftar_karakter:
  time.sleep(0.6)
  print("Kamu memilih Hero", player.capitalize())
else:
  print("Hero tidak ditemukan")
  exit()

# Inventori Player
inventori = []
while True:
  # Menu Utama
  print("===== MENU UTAMA =====")
  print("1.Mulai Bertarung\n2.Inventori & Status\n3.Gacha Item\n4.Keluar game")

  # player milih menu
  menu = int(input("Pilih menu: "))

  # Opsi Mulai Bertarung
  if menu == 1:
    print("Kamu memilih menu bertarung")
    # Mencari Musuh
    print("Mencari Musuh!!")
    time.sleep(0.8)
    random_monster = random.randint(1, 3)
    monster = "goblin" if random_monster == 1 else "orc" if random_monster == 2 else "lizard" if random_monster == 3 else None
    time.sleep(0.8)

    for i in range(5):
      print("Krss..", end="")
      time.sleep(0.8)
    print()

    print("Kamu menemukan monster!")
    print(f"{monster} terlihat!")
    time.sleep(0.8)
    print(f"Hero {player.capitalize()} serang {monster}!")
    time.sleep(0.8)

    # War time
    while daftar_karakter[monster]["hp"] > 0:
      print(f"HP {monster}: {daftar_karakter[monster]['hp']}")
      print(f"HP {player.capitalize()}: {daftar_karakter[player]['hp']}")
      time.sleep(0.6)
      input("Tekan ENTER untuk menyerang!!")

      # Data Pemain
      hp_player = daftar_karakter[player]["hp"]
      atk_player = daftar_karakter[player]["attack"]
      agi_player = daftar_karakter[player]["agility"]
      def_player = daftar_karakter[player]["defense"]

      # Data Musuh
      hp_musuh = daftar_karakter[monster]["hp"]
      atk_musuh = daftar_karakter[monster]["attack"]
      agi_musuh = daftar_karakter[monster]["agility"]
      def_musuh = daftar_karakter[monster]["defense"]

      # Serangan player
      if agi_musuh - agi_player > 10:
        print("Level agility Musuh terlalu tinggi!! Serangan Anda kurang efektif")
      else:
       damage = atk_player - def_musuh
      if damage <= 0:
        damage = 1

      daftar_karakter[monster]["hp"] -= damage
      if daftar_karakter[monster]["hp"] <= 0:
        break

      # Serangan Musuh
      print(f"{monster} menyerang!!")
      time.sleep(0.6)

      if agi_player - agi_musuh > 10:
        print("Level agility Anda terlalu tinggi!!  Serangan musuh kurang efektif")
      else:
        damage = atk_musuh - def_player
      if damage <= 0:
        damage = 1

      daftar_karakter[player]["hp"] -= damage
      if daftar_karakter[player]["hp"] <= 0:
        break

    # Hasil Pertarungan
    if daftar_karakter[player]["hp"] <= 0:
      daftar_karakter[player]["hp"] = 0
      print(f"Hp{monster}: {daftar_karakter[monster]["hp"]}")
      print(f"Anda dikalahkan monster {monster}")
      print(f"Hero {player} Mati!!")
    if daftar_karakter[monster]["hp"] <= 0:
      daftar_karakter[monster]["hp"] = 0
      print(f"Hp {monster}: {daftar_karakter[monster]["hp"]}")
      print(f"Hp {player.capitalize()}:{daftar_karakter[player]["hp"]}")
      print(f"Selamat Hero {player.capitalize()} Anda mengalahkan {monster}!!")

    # Drop item
    drop_monster = random.choice(drop_item)
    if drop_monster in drop_item:
      print(f"Kamu mendapatkan item {drop_monster}")
      inventori.append(drop_monster)
    print(f"Inventori ANda {inventori}")

    # Kembali ke menu utama
    input("Tekan ENTER untuk kembali ke menu utama!!")

  # Menu inventory dan status
  elif menu == 2:
    print(f"===== INVENTORI DAN STATUS {player.capitalize()} =====")
    print(f"Inventori: {inventori}")
    print(f"Status Hero {player.upper()}: {daftar_karakter[player]}")

    # Kembali ke menu utama
    input("Tekan ENTER untuk kembali ke menu utama!!")

  # Menu Gacha Item
  elif menu == 3:
    # List hadiah gacha
    hadiah_common = ["Ramuan", "coin", "Herbal", "Sarung Tangan"]
    hadiah_rare = ["pedang", "panah", "perisai", "kunci"]
    hadiah_legendary = ["Pedang Exalibur", "Perisai Medusa"]

    # Kondisi Hero
    gacha = input("Apakah hero Anda ingin gacha? (x/y): ").lower()

    # gacha
    counter_gacha = 0 # Counter Gacha
    while gacha.lower() == "x":
      persentase = random.randint(1, 100)
      counter_gacha += 1
      print(f"Gacha ke-{counter_gacha}")

      # Hadiah yang didapatkan
      if persentase <= 2 or counter_gacha == 10:
        hadiah = random.choice(hadiah_legendary)
        print(f"Selamat!! Kamu mendapatkan hadiah Legendary: {hadiah}")
        inventori.append(hadiah)
        counter_gacha = 0
        time.sleep(1.5)
   
      elif persentase <= 30:
        hadiah = random.choice(hadiah_rare)
        print(f"Selamat!! Kamu mendapatkan hadiah Rare: {hadiah}")
        inventori.append(hadiah)
        time.sleep(2)

      else:
        hadiah = random.choice(hadiah_common)
        print(f"Selamat!! Kamu mendapatkan hadiah Common: {hadiah}")
        inventori.append(hadiah)
        time.sleep(2)

        print(inventori)

        # Gacha lagi
        gacha = input("Apakah kamu ingin gacha lagi? (x/y): ")
