"""
Enum for all items.
"""
import collections

from .enum_util import AutoLowerNameEnum
from enum import auto, unique


@unique
class Material(AutoLowerNameEnum):
    """
    Contains all of Minecraft's item types (version 1.15.2).
    """
    ACACIA_BOAT = auto()
    ACACIA_BUTTON = auto()
    ACACIA_DOOR = auto()
    ACACIA_FENCE = auto()
    ACACIA_FENCE_GATE = auto()
    ACACIA_LEAVES = auto()
    ACACIA_LOG = auto()
    ACACIA_PLANKS = auto()
    ACACIA_PRESSURE_PLATE = auto()
    ACACIA_SAPLING = auto()
    ACACIA_SIGN = auto()
    ACACIA_SLAB = auto()
    ACACIA_STAIRS = auto()
    ACACIA_TRAPDOOR = auto()
    ACACIA_WOOD = auto()
    ACTIVATOR_RAIL = auto()
    AIR = auto()
    ALLIUM = auto()
    ANDESITE = auto()
    ANDESITE_SLAB = auto()
    ANDESITE_STAIRS = auto()
    ANDESITE_WALL = auto()
    ANVIL = auto()
    APPLE = auto()
    ARMOR_STAND = auto()
    ARROW = auto()
    AZURE_BLUET = auto()
    BAKED_POTATO = auto()
    BAMBOO = auto()
    BARREL = auto()
    BARRIER = auto()
    BAT_SPAWN_EGG = auto()
    BEACON = auto()
    BEDROCK = auto()
    BEE_NEST = auto()
    BEE_SPAWN_EGG = auto()
    BEEF = auto()
    BEEHIVE = auto()
    BEETROOT = auto()
    BEETROOT_SEEDS = auto()
    BEETROOT_SOUP = auto()
    BELL = auto()
    BIRCH_BOAT = auto()
    BIRCH_BUTTON = auto()
    BIRCH_DOOR = auto()
    BIRCH_FENCE = auto()
    BIRCH_FENCE_GATE = auto()
    BIRCH_LEAVES = auto()
    BIRCH_LOG = auto()
    BIRCH_PLANKS = auto()
    BIRCH_PRESSURE_PLATE = auto()
    BIRCH_SAPLING = auto()
    BIRCH_SIGN = auto()
    BIRCH_SLAB = auto()
    BIRCH_STAIRS = auto()
    BIRCH_TRAPDOOR = auto()
    BIRCH_WOOD = auto()
    BLACK_BANNER = auto()
    BLACK_BED = auto()
    BLACK_CARPET = auto()
    BLACK_CONCRETE = auto()
    BLACK_CONCRETE_POWDER = auto()
    BLACK_DYE = auto()
    BLACK_GLAZED_TERRACOTTA = auto()
    BLACK_SHULKER_BOX = auto()
    BLACK_STAINED_GLASS = auto()
    BLACK_STAINED_GLASS_PANE = auto()
    BLACK_TERRACOTTA = auto()
    BLACK_WOOL = auto()
    BLAST_FURNACE = auto()
    BLAZE_POWDER = auto()
    BLAZE_ROD = auto()
    BLAZE_SPAWN_EGG = auto()
    BLUE_BANNER = auto()
    BLUE_BED = auto()
    BLUE_CARPET = auto()
    BLUE_CONCRETE = auto()
    BLUE_CONCRETE_POWDER = auto()
    BLUE_DYE = auto()
    BLUE_GLAZED_TERRACOTTA = auto()
    BLUE_ICE = auto()
    BLUE_ORCHID = auto()
    BLUE_SHULKER_BOX = auto()
    BLUE_STAINED_GLASS = auto()
    BLUE_STAINED_GLASS_PANE = auto()
    BLUE_TERRACOTTA = auto()
    BLUE_WOOL = auto()
    BONE = auto()
    BONE_BLOCK = auto()
    BONE_MEAL = auto()
    BOOK = auto()
    BOOKSHELF = auto()
    BOW = auto()
    BOWL = auto()
    BRAIN_CORAL = auto()
    BRAIN_CORAL_BLOCK = auto()
    BRAIN_CORAL_FAN = auto()
    BREAD = auto()
    BREWING_STAND = auto()
    BRICK = auto()
    BRICK_SLAB = auto()
    BRICK_STAIRS = auto()
    BRICK_WALL = auto()
    BRICKS = auto()
    BROWN_BANNER = auto()
    BROWN_BED = auto()
    BROWN_CARPET = auto()
    BROWN_CONCRETE = auto()
    BROWN_CONCRETE_POWDER = auto()
    BROWN_DYE = auto()
    BROWN_GLAZED_TERRACOTTA = auto()
    BROWN_MUSHROOM = auto()
    BROWN_MUSHROOM_BLOCK = auto()
    BROWN_SHULKER_BOX = auto()
    BROWN_STAINED_GLASS = auto()
    BROWN_STAINED_GLASS_PANE = auto()
    BROWN_TERRACOTTA = auto()
    BROWN_WOOL = auto()
    BUBBLE_CORAL = auto()
    BUBBLE_CORAL_BLOCK = auto()
    BUBBLE_CORAL_FAN = auto()
    BUCKET = auto()
    CACTUS = auto()
    CAKE = auto()
    CAMPFIRE = auto()
    CARROT = auto()
    CARROT_ON_A_STICK = auto()
    CARTOGRAPHY_TABLE = auto()
    CARVED_PUMPKIN = auto()
    CAT_SPAWN_EGG = auto()
    CAULDRON = auto()
    CAVE_SPIDER_SPAWN_EGG = auto()
    CHAIN_COMMAND_BLOCK = auto()
    CHAINMAIL_BOOTS = auto()
    CHAINMAIL_CHESTPLATE = auto()
    CHAINMAIL_HELMET = auto()
    CHAINMAIL_LEGGINGS = auto()
    CHARCOAL = auto()
    CHEST = auto()
    CHEST_MINECART = auto()
    CHICKEN = auto()
    CHICKEN_SPAWN_EGG = auto()
    CHIPPED_ANVIL = auto()
    CHISELED_QUARTZ_BLOCK = auto()
    CHISELED_RED_SANDSTONE = auto()
    CHISELED_SANDSTONE = auto()
    CHISELED_STONE_BRICKS = auto()
    CHORUS_FLOWER = auto()
    CHORUS_FRUIT = auto()
    CHORUS_PLANT = auto()
    CLAY = auto()
    CLAY_BALL = auto()
    CLOCK = auto()
    COAL = auto()
    COAL_BLOCK = auto()
    COAL_ORE = auto()
    COARSE_DIRT = auto()
    COBBLESTONE = auto()
    COBBLESTONE_SLAB = auto()
    COBBLESTONE_STAIRS = auto()
    COBBLESTONE_WALL = auto()
    COBWEB = auto()
    COCOA_BEANS = auto()
    COD = auto()
    COD_BUCKET = auto()
    COD_SPAWN_EGG = auto()
    COMMAND_BLOCK = auto()
    COMMAND_BLOCK_MINECART = auto()
    COMPARATOR = auto()
    COMPASS = auto()
    COMPOSTER = auto()
    CONDUIT = auto()
    COOKED_BEEF = auto()
    COOKED_CHICKEN = auto()
    COOKED_COD = auto()
    COOKED_MUTTON = auto()
    COOKED_PORKCHOP = auto()
    COOKED_RABBIT = auto()
    COOKED_SALMON = auto()
    COOKIE = auto()
    CORNFLOWER = auto()
    COW_SPAWN_EGG = auto()
    CRACKED_STONE_BRICKS = auto()
    CRAFTING_TABLE = auto()
    CREEPER_BANNER_PATTERN = auto()
    CREEPER_HEAD = auto()
    CREEPER_SPAWN_EGG = auto()
    CROSSBOW = auto()
    CUT_RED_SANDSTONE = auto()
    CUT_RED_SANDSTONE_SLAB = auto()
    CUT_SANDSTONE = auto()
    CUT_SANDSTONE_SLAB = auto()
    CYAN_BANNER = auto()
    CYAN_BED = auto()
    CYAN_CARPET = auto()
    CYAN_CONCRETE = auto()
    CYAN_CONCRETE_POWDER = auto()
    CYAN_DYE = auto()
    CYAN_GLAZED_TERRACOTTA = auto()
    CYAN_SHULKER_BOX = auto()
    CYAN_STAINED_GLASS = auto()
    CYAN_STAINED_GLASS_PANE = auto()
    CYAN_TERRACOTTA = auto()
    CYAN_WOOL = auto()
    DAMAGED_ANVIL = auto()
    DANDELION = auto()
    DARK_OAK_BOAT = auto()
    DARK_OAK_BUTTON = auto()
    DARK_OAK_DOOR = auto()
    DARK_OAK_FENCE = auto()
    DARK_OAK_FENCE_GATE = auto()
    DARK_OAK_LEAVES = auto()
    DARK_OAK_LOG = auto()
    DARK_OAK_PLANKS = auto()
    DARK_OAK_PRESSURE_PLATE = auto()
    DARK_OAK_SAPLING = auto()
    DARK_OAK_SIGN = auto()
    DARK_OAK_SLAB = auto()
    DARK_OAK_STAIRS = auto()
    DARK_OAK_TRAPDOOR = auto()
    DARK_OAK_WOOD = auto()
    DARK_PRISMARINE = auto()
    DARK_PRISMARINE_SLAB = auto()
    DARK_PRISMARINE_STAIRS = auto()
    DAYLIGHT_DETECTOR = auto()
    DEAD_BRAIN_CORAL = auto()
    DEAD_BRAIN_CORAL_BLOCK = auto()
    DEAD_BRAIN_CORAL_FAN = auto()
    DEAD_BUBBLE_CORAL = auto()
    DEAD_BUBBLE_CORAL_BLOCK = auto()
    DEAD_BUBBLE_CORAL_FAN = auto()
    DEAD_BUSH = auto()
    DEAD_FIRE_CORAL = auto()
    DEAD_FIRE_CORAL_BLOCK = auto()
    DEAD_FIRE_CORAL_FAN = auto()
    DEAD_HORN_CORAL = auto()
    DEAD_HORN_CORAL_BLOCK = auto()
    DEAD_HORN_CORAL_FAN = auto()
    DEAD_TUBE_CORAL = auto()
    DEAD_TUBE_CORAL_BLOCK = auto()
    DEAD_TUBE_CORAL_FAN = auto()
    DETECTOR_RAIL = auto()
    DIAMOND = auto()
    DIAMOND_AXE = auto()
    DIAMOND_BLOCK = auto()
    DIAMOND_BOOTS = auto()
    DIAMOND_CHESTPLATE = auto()
    DIAMOND_HELMET = auto()
    DIAMOND_HOE = auto()
    DIAMOND_HORSE_ARMOR = auto()
    DIAMOND_LEGGINGS = auto()
    DIAMOND_ORE = auto()
    DIAMOND_PICKAXE = auto()
    DIAMOND_SHOVEL = auto()
    DIAMOND_SWORD = auto()
    DIORITE = auto()
    DIORITE_SLAB = auto()
    DIORITE_STAIRS = auto()
    DIORITE_WALL = auto()
    DIRT = auto()
    DISPENSER = auto()
    DOLPHIN_SPAWN_EGG = auto()
    DONKEY_SPAWN_EGG = auto()
    DRAGON_BREATH = auto()
    DRAGON_EGG = auto()
    DRAGON_HEAD = auto()
    DRIED_KELP = auto()
    DRIED_KELP_BLOCK = auto()
    DROPPER = auto()
    DROWNED_SPAWN_EGG = auto()
    EGG = auto()
    ELDER_GUARDIAN_SPAWN_EGG = auto()
    ELYTRA = auto()
    EMERALD = auto()
    EMERALD_BLOCK = auto()
    EMERALD_ORE = auto()
    ENCHANTED_BOOK = auto()
    ENCHANTED_GOLDEN_APPLE = auto()
    ENCHANTING_TABLE = auto()
    END_CRYSTAL = auto()
    END_PORTAL_FRAME = auto()
    END_ROD = auto()
    END_STONE = auto()
    END_STONE_BRICK_SLAB = auto()
    END_STONE_BRICK_STAIRS = auto()
    END_STONE_BRICK_WALL = auto()
    END_STONE_BRICKS = auto()
    ENDER_CHEST = auto()
    ENDER_EYE = auto()
    ENDER_PEARL = auto()
    ENDERMAN_SPAWN_EGG = auto()
    ENDERMITE_SPAWN_EGG = auto()
    EVOKER_SPAWN_EGG = auto()
    EXPERIENCE_BOTTLE = auto()
    FARMLAND = auto()
    FEATHER = auto()
    FERMENTED_SPIDER_EYE = auto()
    FERN = auto()
    FILLED_MAP = auto()
    FIRE_CHARGE = auto()
    FIRE_CORAL = auto()
    FIRE_CORAL_BLOCK = auto()
    FIRE_CORAL_FAN = auto()
    FIREWORK_ROCKET = auto()
    FIREWORK_STAR = auto()
    FISHING_ROD = auto()
    FLETCHING_TABLE = auto()
    FLINT = auto()
    FLINT_AND_STEEL = auto()
    FLOWER_BANNER_PATTERN = auto()
    FLOWER_POT = auto()
    FOX_SPAWN_EGG = auto()
    FURNACE = auto()
    FURNACE_MINECART = auto()
    GHAST_SPAWN_EGG = auto()
    GHAST_TEAR = auto()
    GLASS = auto()
    GLASS_BOTTLE = auto()
    GLASS_PANE = auto()
    GLISTERING_MELON_SLICE = auto()
    GLOBE_BANNER_PATTERN = auto()
    GLOWSTONE = auto()
    GLOWSTONE_DUST = auto()
    GOLD_BLOCK = auto()
    GOLD_INGOT = auto()
    GOLD_NUGGET = auto()
    GOLD_ORE = auto()
    GOLDEN_APPLE = auto()
    GOLDEN_AXE = auto()
    GOLDEN_BOOTS = auto()
    GOLDEN_CARROT = auto()
    GOLDEN_CHESTPLATE = auto()
    GOLDEN_HELMET = auto()
    GOLDEN_HOE = auto()
    GOLDEN_HORSE_ARMOR = auto()
    GOLDEN_LEGGINGS = auto()
    GOLDEN_PICKAXE = auto()
    GOLDEN_SHOVEL = auto()
    GOLDEN_SWORD = auto()
    GRANITE = auto()
    GRANITE_SLAB = auto()
    GRANITE_STAIRS = auto()
    GRANITE_WALL = auto()
    GRASS = auto()
    GRASS_BLOCK = auto()
    GRASS_PATH = auto()
    GRAVEL = auto()
    GRAY_BANNER = auto()
    GRAY_BED = auto()
    GRAY_CARPET = auto()
    GRAY_CONCRETE = auto()
    GRAY_CONCRETE_POWDER = auto()
    GRAY_DYE = auto()
    GRAY_GLAZED_TERRACOTTA = auto()
    GRAY_SHULKER_BOX = auto()
    GRAY_STAINED_GLASS = auto()
    GRAY_STAINED_GLASS_PANE = auto()
    GRAY_TERRACOTTA = auto()
    GRAY_WOOL = auto()
    GREEN_BANNER = auto()
    GREEN_BED = auto()
    GREEN_CARPET = auto()
    GREEN_CONCRETE = auto()
    GREEN_CONCRETE_POWDER = auto()
    GREEN_DYE = auto()
    GREEN_GLAZED_TERRACOTTA = auto()
    GREEN_SHULKER_BOX = auto()
    GREEN_STAINED_GLASS = auto()
    GREEN_STAINED_GLASS_PANE = auto()
    GREEN_TERRACOTTA = auto()
    GREEN_WOOL = auto()
    GRINDSTONE = auto()
    GUARDIAN_SPAWN_EGG = auto()
    GUNPOWDER = auto()
    HAY_BLOCK = auto()
    HEART_OF_THE_SEA = auto()
    HEAVY_WEIGHTED_PRESSURE_PLATE = auto()
    HONEY_BLOCK = auto()
    HONEY_BOTTLE = auto()
    HONEY_COMB = auto()
    HONEYCOMB_BLOCK = auto()
    HOPPER = auto()
    HOPPER_MINECART = auto()
    HORN_CORAL = auto()
    HORN_CORAL_BLOCK = auto()
    HORN_CORAL_FAN = auto()
    HORSE_SPAWN_EGG = auto()
    HUSK_SPAWN_EGG = auto()
    ICE = auto()
    INFESTED_CHISELED_STONE_BRICKS = auto()
    INFESTED_COBBLESTONE = auto()
    INFESTED_CRACKED_STONE_BRICKS = auto()
    INFESTED_MOSSY_STONE_BRICKS = auto()
    INFESTED_STONE = auto()
    INFESTED_STONE_BRICKS = auto()
    INK_SAC = auto()
    IRON_AXE = auto()
    IRON_BARS = auto()
    IRON_BLOCK = auto()
    IRON_BOOTS = auto()
    IRON_CHESTPLATE = auto()
    IRON_DOOR = auto()
    IRON_HELMET = auto()
    IRON_HOE = auto()
    IRON_HORSE_ARMOR = auto()
    IRON_INGOT = auto()
    IRON_LEGGINGS = auto()
    IRON_NUGGET = auto()
    IRON_ORE = auto()
    IRON_PICKAXE = auto()
    IRON_SHOVEL = auto()
    IRON_SWORD = auto()
    IRON_TRAPDOOR = auto()
    ITEM_FRAME = auto()
    JACK_O_LANTERN = auto()
    JUKEBOX = auto()
    JUNGLE_BOAT = auto()
    JUNGLE_BUTTON = auto()
    JUNGLE_DOOR = auto()
    JUNGLE_FENCE = auto()
    JUNGLE_FENCE_GATE = auto()
    JUNGLE_LEAVES = auto()
    JUNGLE_LOG = auto()
    JUNGLE_PLANKS = auto()
    JUNGLE_PRESSURE_PLATE = auto()
    JUNGLE_SAPLING = auto()
    JUNGLE_SIGN = auto()
    JUNGLE_SLAB = auto()
    JUNGLE_STAIRS = auto()
    JUNGLE_TRAPDOOR = auto()
    JUNGLE_WOOD = auto()
    KELP = auto()
    LADDER = auto()
    LANTERN = auto()
    LAPIS_BLOCK = auto()
    LAPIS_LAZULI = auto()
    LAPIS_ORE = auto()
    LARGE_FERN = auto()
    LAVA_BUCKET = auto()
    LEAD = auto()
    LEATHER = auto()
    LEATHER_BOOTS = auto()
    LEATHER_CHESTPLATE = auto()
    LEATHER_HELMET = auto()
    LEATHER_HORSE_ARMOR = auto()
    LEATHER_LEGGINGS = auto()
    LECTERN = auto()
    LEVER = auto()
    LIGHT_BLUE_BANNER = auto()
    LIGHT_BLUE_BED = auto()
    LIGHT_BLUE_CARPET = auto()
    LIGHT_BLUE_CONCRETE = auto()
    LIGHT_BLUE_CONCRETE_POWDER = auto()
    LIGHT_BLUE_DYE = auto()
    LIGHT_BLUE_GLAZED_TERRACOTTA = auto()
    LIGHT_BLUE_SHULKER_BOX = auto()
    LIGHT_BLUE_STAINED_GLASS = auto()
    LIGHT_BLUE_STAINED_GLASS_PANE = auto()
    LIGHT_BLUE_TERRACOTTA = auto()
    LIGHT_BLUE_WOOL = auto()
    LIGHT_GRAY_BANNER = auto()
    LIGHT_GRAY_BED = auto()
    LIGHT_GRAY_CARPET = auto()
    LIGHT_GRAY_CONCRETE = auto()
    LIGHT_GRAY_CONCRETE_POWDER = auto()
    LIGHT_GRAY_DYE = auto()
    LIGHT_GRAY_GLAZED_TERRACOTTA = auto()
    LIGHT_GRAY_SHULKER_BOX = auto()
    LIGHT_GRAY_STAINED_GLASS = auto()
    LIGHT_GRAY_STAINED_GLASS_PANE = auto()
    LIGHT_GRAY_TERRACOTTA = auto()
    LIGHT_GRAY_WOOL = auto()
    LIGHT_WEIGHTED_PRESSURE_PLATE = auto()
    LILAC = auto()
    LILY_OF_THE_VALLEY = auto()
    LILY_PAD = auto()
    LIME_BANNER = auto()
    LIME_BED = auto()
    LIME_CARPET = auto()
    LIME_CONCRETE = auto()
    LIME_CONCRETE_POWDER = auto()
    LIME_DYE = auto()
    LIME_GLAZED_TERRACOTTA = auto()
    LIME_SHULKER_BOX = auto()
    LIME_STAINED_GLASS = auto()
    LIME_STAINED_GLASS_PANE = auto()
    LIME_TERRACOTTA = auto()
    LIME_WOOL = auto()
    LINGERING_POTION = auto()
    LLAMA_SPAWN_EGG = auto()
    LOOM = auto()
    MAGENTA_BANNER = auto()
    MAGENTA_BED = auto()
    MAGENTA_CARPET = auto()
    MAGENTA_CONCRETE = auto()
    MAGENTA_CONCRETE_POWDER = auto()
    MAGENTA_DYE = auto()
    MAGENTA_GLAZED_TERRACOTTA = auto()
    MAGENTA_SHULKER_BOX = auto()
    MAGENTA_STAINED_GLASS = auto()
    MAGENTA_STAINED_GLASS_PANE = auto()
    MAGENTA_TERRACOTTA = auto()
    MAGENTA_WOOL = auto()
    MAGMA_BLOCK = auto()
    MAGMA_CREAM = auto()
    MAGMA_CUBE_SPAWN_EGG = auto()
    MAP = auto()
    MELON = auto()
    MELON_SEEDS = auto()
    MELON_SLICE = auto()
    MILK_BUCKET = auto()
    MINECART = auto()
    MOJANG_BANNER_PATTERN = auto()
    MOOSHROOM_SPAWN_EGG = auto()
    MOSSY_COBBLESTONE = auto()
    MOSSY_COBBLESTONE_SLAB = auto()
    MOSSY_COBBLESTONE_STAIRS = auto()
    MOSSY_COBBLESTONE_WALL = auto()
    MOSSY_STONE_BRICK_SLAB = auto()
    MOSSY_STONE_BRICK_STAIRS = auto()
    MOSSY_STONE_BRICK_WALL = auto()
    MOSSY_STONE_BRICKS = auto()
    MULE_SPAWN_EGG = auto()
    MUSHROOM_STEM = auto()
    MUSHROOM_STEW = auto()
    MUSIC_DISC_11 = auto()
    MUSIC_DISC_13 = auto()
    MUSIC_DISC_BLOCKS = auto()
    MUSIC_DISC_CAT = auto()
    MUSIC_DISC_CHIRP = auto()
    MUSIC_DISC_FAR = auto()
    MUSIC_DISC_MALL = auto()
    MUSIC_DISC_MELLOHI = auto()
    MUSIC_DISC_STAL = auto()
    MUSIC_DISC_STRAD = auto()
    MUSIC_DISC_WAIT = auto()
    MUSIC_DISC_WARD = auto()
    MUTTON = auto()
    MYCELIUM = auto()
    NAME_TAG = auto()
    NAUTILUS_SHELL = auto()
    NETHER_BRICK = auto()
    NETHER_BRICK_FENCE = auto()
    NETHER_BRICK_SLAB = auto()
    NETHER_BRICK_STAIRS = auto()
    NETHER_BRICK_WALL = auto()
    NETHER_BRICKS = auto()
    NETHER_QUARTZ_ORE = auto()
    NETHER_STAR = auto()
    NETHER_WART = auto()
    NETHER_WART_BLOCK = auto()
    NETHERRACK = auto()
    NOTE_BLOCK = auto()
    OAK_BOAT = auto()
    OAK_BUTTON = auto()
    OAK_DOOR = auto()
    OAK_FENCE = auto()
    OAK_FENCE_GATE = auto()
    OAK_LEAVES = auto()
    OAK_LOG = auto()
    OAK_PLANKS = auto()
    OAK_PRESSURE_PLATE = auto()
    OAK_SAPLING = auto()
    OAK_SIGN = auto()
    OAK_SLAB = auto()
    OAK_STAIRS = auto()
    OAK_TRAPDOOR = auto()
    OAK_WOOD = auto()
    OBSERVER = auto()
    OBSIDIAN = auto()
    OCELOT_SPAWN_EGG = auto()
    ORANGE_BANNER = auto()
    ORANGE_BED = auto()
    ORANGE_CARPET = auto()
    ORANGE_CONCRETE = auto()
    ORANGE_CONCRETE_POWDER = auto()
    ORANGE_DYE = auto()
    ORANGE_GLAZED_TERRACOTTA = auto()
    ORANGE_SHULKER_BOX = auto()
    ORANGE_STAINED_GLASS = auto()
    ORANGE_STAINED_GLASS_PANE = auto()
    ORANGE_TERRACOTTA = auto()
    ORANGE_TULIP = auto()
    ORANGE_WOOL = auto()
    OXEYE_DAISY = auto()
    PACKED_ICE = auto()
    PAINTING = auto()
    PANDA_SPAWN_EGG = auto()
    PAPER = auto()
    PARROT_SPAWN_EGG = auto()
    PEONY = auto()
    PETRIFIED_OAK_SLAB = auto()
    PHANTOM_MEMBRANE = auto()
    PHANTOM_SPAWN_EGG = auto()
    PIG_SPAWN_EGG = auto()
    PILLAGER_SPAWN_EGG = auto()
    PINK_BANNER = auto()
    PINK_BED = auto()
    PINK_CARPET = auto()
    PINK_CONCRETE = auto()
    PINK_CONCRETE_POWDER = auto()
    PINK_DYE = auto()
    PINK_GLAZED_TERRACOTTA = auto()
    PINK_SHULKER_BOX = auto()
    PINK_STAINED_GLASS = auto()
    PINK_STAINED_GLASS_PANE = auto()
    PINK_TERRACOTTA = auto()
    PINK_TULIP = auto()
    PINK_WOOL = auto()
    PISTON = auto()
    PLAYER_HEAD = auto()
    PODZOL = auto()
    POISONOUS_POTATO = auto()
    POLAR_BEAR_SPAWN_EGG = auto()
    POLISHED_ANDESITE = auto()
    POLISHED_ANDESITE_SLAB = auto()
    POLISHED_ANDESITE_STAIRS = auto()
    POLISHED_DIORITE = auto()
    POLISHED_DIORITE_SLAB = auto()
    POLISHED_DIORITE_STAIRS = auto()
    POLISHED_GRANITE = auto()
    POLISHED_GRANITE_SLAB = auto()
    POLISHED_GRANITE_STAIRS = auto()
    POPPED_CHORUS_FRUIT = auto()
    POPPY = auto()
    PORKCHOP = auto()
    POTATO = auto()
    POTION = auto()
    POWERED_RAIL = auto()
    PRISMARINE = auto()
    PRISMARINE_BRICK_SLAB = auto()
    PRISMARINE_BRICK_STAIRS = auto()
    PRISMARINE_BRICKS = auto()
    PRISMARINE_CRYSTALS = auto()
    PRISMARINE_SHARD = auto()
    PRISMARINE_SLAB = auto()
    PRISMARINE_STAIRS = auto()
    PRISMARINE_WALL = auto()
    PUFFERFISH = auto()
    PUFFERFISH_BUCKET = auto()
    PUFFERFISH_SPAWN_EGG = auto()
    PUMPKIN = auto()
    PUMPKIN_PIE = auto()
    PUMPKIN_SEEDS = auto()
    PURPLE_BANNER = auto()
    PURPLE_BED = auto()
    PURPLE_CARPET = auto()
    PURPLE_CONCRETE = auto()
    PURPLE_CONCRETE_POWDER = auto()
    PURPLE_DYE = auto()
    PURPLE_GLAZED_TERRACOTTA = auto()
    PURPLE_SHULKER_BOX = auto()
    PURPLE_STAINED_GLASS = auto()
    PURPLE_STAINED_GLASS_PANE = auto()
    PURPLE_TERRACOTTA = auto()
    PURPLE_WOOL = auto()
    PURPUR_BLOCK = auto()
    PURPUR_PILLAR = auto()
    PURPUR_SLAB = auto()
    PURPUR_STAIRS = auto()
    QUARTZ = auto()
    QUARTZ_BLOCK = auto()
    QUARTZ_PILLAR = auto()
    QUARTZ_SLAB = auto()
    QUARTZ_STAIRS = auto()
    RABBIT = auto()
    RABBIT_FOOT = auto()
    RABBIT_HIDE = auto()
    RABBIT_SPAWN_EGG = auto()
    RABBIT_STEW = auto()
    RAIL = auto()
    RAVAGER_SPAWN_EGG = auto()
    RED_BANNER = auto()
    RED_BED = auto()
    RED_CARPET = auto()
    RED_CONCRETE = auto()
    RED_CONCRETE_POWDER = auto()
    RED_DYE = auto()
    RED_GLAZED_TERRACOTTA = auto()
    RED_MUSHROOM = auto()
    RED_MUSHROOM_BLOCK = auto()
    RED_NETHER_BRICK_SLAB = auto()
    RED_NETHER_BRICK_STAIRS = auto()
    RED_NETHER_BRICK_WALL = auto()
    RED_NETHER_BRICKS = auto()
    RED_SAND = auto()
    RED_SANDSTONE = auto()
    RED_SANDSTONE_SLAB = auto()
    RED_SANDSTONE_STAIRS = auto()
    RED_SANDSTONE_WALL = auto()
    RED_SHULKER_BOX = auto()
    RED_STAINED_GLASS = auto()
    RED_STAINED_GLASS_PANE = auto()
    RED_TERRACOTTA = auto()
    RED_TULIP = auto()
    RED_WOOL = auto()
    REDSTONE = auto()
    REDSTONE_BLOCK = auto()
    REDSTONE_LAMP = auto()
    REDSTONE_ORE = auto()
    REDSTONE_TORCH = auto()
    REPEATER = auto()
    REPEATING_COMMAND_BLOCK = auto()
    ROSE_BUSH = auto()
    ROTTEN_FLESH = auto()
    SADDLE = auto()
    SALMON = auto()
    SALMON_BUCKET = auto()
    SALMON_SPAWN_EGG = auto()
    SAND = auto()
    SANDSTONE = auto()
    SANDSTONE_SLAB = auto()
    SANDSTONE_STAIRS = auto()
    SANDSTONE_WALL = auto()
    SCAFFOLDING = auto()
    SCUTE = auto()
    SEA_LANTERN = auto()
    SEA_PICKLE = auto()
    SEAGRASS = auto()
    SHEARS = auto()
    SHEEP_SPAWN_EGG = auto()
    SHIELD = auto()
    SHULKER_BOX = auto()
    SHULKER_SHELL = auto()
    SHULKER_SPAWN_EGG = auto()
    SILVERFISH_SPAWN_EGG = auto()
    SKELETON_HORSE_SPAWN_EGG = auto()
    SKELETON_SKULL = auto()
    SKELETON_SPAWN_EGG = auto()
    SKULL_BANNER_PATTERN = auto()
    SLIME_BALL = auto()
    SLIME_BLOCK = auto()
    SLIME_SPAWN_EGG = auto()
    SMITHING_TABLE = auto()
    SMOKER = auto()
    SMOOTH_QUARTZ = auto()
    SMOOTH_QUARTZ_SLAB = auto()
    SMOOTH_QUARTZ_STAIRS = auto()
    SMOOTH_RED_SANDSTONE = auto()
    SMOOTH_RED_SANDSTONE_SLAB = auto()
    SMOOTH_RED_SANDSTONE_STAIRS = auto()
    SMOOTH_SANDSTONE = auto()
    SMOOTH_SANDSTONE_SLAB = auto()
    SMOOTH_SANDSTONE_STAIRS = auto()
    SMOOTH_STONE = auto()
    SMOOTH_STONE_SLAB = auto()
    SNOW = auto()
    SNOW_BLOCK = auto()
    SNOWBALL = auto()
    SOUL_SAND = auto()
    SPAWNER = auto()
    SPECTRAL_ARROW = auto()
    SPIDER_EYE = auto()
    SPIDER_SPAWN_EGG = auto()
    SPLASH_POTION = auto()
    SPONGE = auto()
    SPRUCE_BOAT = auto()
    SPRUCE_BUTTON = auto()
    SPRUCE_DOOR = auto()
    SPRUCE_FENCE = auto()
    SPRUCE_FENCE_GATE = auto()
    SPRUCE_LEAVES = auto()
    SPRUCE_LOG = auto()
    SPRUCE_PLANKS = auto()
    SPRUCE_PRESSURE_PLATE = auto()
    SPRUCE_SAPLING = auto()
    SPRUCE_SIGN = auto()
    SPRUCE_SLAB = auto()
    SPRUCE_STAIRS = auto()
    SPRUCE_TRAPDOOR = auto()
    SPRUCE_WOOD = auto()
    SQUID_SPAWN_EGG = auto()
    STICK = auto()
    STICKY_PISTON = auto()
    STONE = auto()
    STONE_AXE = auto()
    STONE_BRICK_SLAB = auto()
    STONE_BRICK_STAIRS = auto()
    STONE_BRICK_WALL = auto()
    STONE_BRICKS = auto()
    STONE_BUTTON = auto()
    STONE_HOE = auto()
    STONE_PICKAXE = auto()
    STONE_PRESSURE_PLATE = auto()
    STONE_SHOVEL = auto()
    STONE_SLAB = auto()
    STONE_STAIRS = auto()
    STONE_SWORD = auto()
    STRAY_SPAWN_EGG = auto()
    STRING = auto()
    STRIPPED_ACACIA_LOG = auto()
    STRIPPED_ACACIA_WOOD = auto()
    STRIPPED_BIRCH_LOG = auto()
    STRIPPED_BIRCH_WOOD = auto()
    STRIPPED_DARK_OAK_LOG = auto()
    STRIPPED_DARK_OAK_WOOD = auto()
    STRIPPED_JUNGLE_LOG = auto()
    STRIPPED_JUNGLE_WOOD = auto()
    STRIPPED_OAK_LOG = auto()
    STRIPPED_OAK_WOOD = auto()
    STRIPPED_SPRUCE_LOG = auto()
    STRIPPED_SPRUCE_WOOD = auto()
    STRUCTURE_BLOCK = auto()
    STRUCTURE_VOID = auto()
    SUGAR = auto()
    SUGAR_CANE = auto()
    SUNFLOWER = auto()
    SUSPICIOUS_STEW = auto()
    SWEET_BERRIES = auto()
    TALL_GRASS = auto()
    TERRACOTTA = auto()
    TIPPED_ARROW = auto()
    TNT = auto()
    TNT_MINECART = auto()
    TORCH = auto()
    TOTEM_OF_UNDYING = auto()
    TRADER_LLAMA_SPAWN_EGG = auto()
    TRAPPED_CHEST = auto()
    TRIDENT = auto()
    TRIPWIRE_HOOK = auto()
    TROPICAL_FISH = auto()
    TROPICAL_FISH_BUCKET = auto()
    TROPICAL_FISH_SPAWN_EGG = auto()
    TUBE_CORAL = auto()
    TUBE_CORAL_BLOCK = auto()
    TUBE_CORAL_FAN = auto()
    TURTLE_EGG = auto()
    TURTLE_HELMET = auto()
    TURTLE_SPAWN_EGG = auto()
    VEX_SPAWN_EGG = auto()
    VILLAGER_SPAWN_EGG = auto()
    VINDICATOR_SPAWN_EGG = auto()
    VINE = auto()
    WANDERING_TRADER_SPAWN_EGG = auto()
    WATER_BUCKET = auto()
    WET_SPONGE = auto()
    WHEAT = auto()
    WHEAT_SEEDS = auto()
    WHITE_BANNER = auto()
    WHITE_BED = auto()
    WHITE_CARPET = auto()
    WHITE_CONCRETE = auto()
    WHITE_CONCRETE_POWDER = auto()
    WHITE_DYE = auto()
    WHITE_GLAZED_TERRACOTTA = auto()
    WHITE_SHULKER_BOX = auto()
    WHITE_STAINED_GLASS = auto()
    WHITE_STAINED_GLASS_PANE = auto()
    WHITE_TERRACOTTA = auto()
    WHITE_TULIP = auto()
    WHITE_WOOL = auto()
    WITCH_SPAWN_EGG = auto()
    WITHER_ROSE = auto()
    WITHER_SKELETON_SKULL = auto()
    WITHER_SKELETON_SPAWN_EGG = auto()
    WOLF_SPAWN_EGG = auto()
    WOODEN_AXE = auto()
    WOODEN_HOE = auto()
    WOODEN_PICKAXE = auto()
    WOODEN_SHOVEL = auto()
    WOODEN_SWORD = auto()
    WRITABLE_BOOK = auto()
    WRITTEN_BOOK = auto()
    YELLOW_BANNER = auto()
    YELLOW_BED = auto()
    YELLOW_CARPET = auto()
    YELLOW_CONCRETE = auto()
    YELLOW_CONCRETE_POWDER = auto()
    YELLOW_DYE = auto()
    YELLOW_GLAZED_TERRACOTTA = auto()
    YELLOW_SHULKER_BOX = auto()
    YELLOW_STAINED_GLASS = auto()
    YELLOW_STAINED_GLASS_PANE = auto()
    YELLOW_TERRACOTTA = auto()
    YELLOW_WOOL = auto()
    ZOMBIE_HEAD = auto()
    ZOMBIE_HORSE_SPAWN_EGG = auto()
    ZOMBIE_PIGMAN_SPAWN_EGG = auto()
    ZOMBIE_SPAWN_EGG = auto()
    ZOMBIE_VILLAGER_SPAWN_EGG = auto()


def _material_new(cls, value):  # allow `minecraft:`
    if isinstance(value, (str, collections.UserString)) and str(value).startswith("minecraft:"):
        value = str(value).replace("minecraft:", "")

    return super(Material, cls).__new__(cls, value)


setattr(Material, "__new__", _material_new)
