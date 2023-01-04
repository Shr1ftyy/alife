# ZOOM_SCALE = 4 * 0.01
WORLD_SCALER:int = 1
FOODSIZE:int = (WORLD_SCALER * 20, WORLD_SCALER * 20)
MAX_FOOD:int = 100
FOOD_ENERGY: int = 300

# Creatures
ANTENNA_RANGE_SCALER = 3
SENSOR_RANGE:int = 4
MAX_ANGLE_RATE:int = 10
MAX_SPEED:int = 5
MIN_CREATURE_SIZE:int = WORLD_SCALER * 20
MAX_CREATURE_SIZE:int = WORLD_SCALER * 40
MAX_ENERGY_CAP = 1600
MIN_ENERGY_CAP = 800
MIN_ENERGY_LOSS_RATE = 1
MAX_ENERGY_LOSS_RATE = 2
MIN_CREATURE_VIEW_DIST:int = WORLD_SCALER * 10
MAX_CREATURE_VIEW_DIST:int = WORLD_SCALER * 60
MIN_MUTATION_RATE = 0.02
MAX_MUTATION_RATE = 0.2
WORLDSIZE = (WORLD_SCALER * 1500, WORLD_SCALER * 1500)
# TODO: cannot call mutateGenes with just 1 creature - fix error in the future 
NUM_CREATURES:int = 20

MIN_DMG = MIN_ENERGY_CAP/4
MAX_DMG = MIN_ENERGY_CAP/2
MIN_DMG_COST = MIN_DMG/20
MAX_DMG_COST = MIN_DMG/10

MIN_BIRTH_COST = MIN_ENERGY_CAP/3
MAX_BIRTH_COST = MIN_ENERGY_CAP/2

TORCH_SEED = 69
DB_UPDATE_INC=1
MAX_FPS=240