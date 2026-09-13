from datetime import datetime , timedelta


# ============================================================
# FITNESS APP
# EXERCISE KNOWLEDGE SYSTEM
# PART 1 — CORE DATABASES
# ============================================================


# ============================================================
# 1. MUSCLE DATABASE
# ============================================================
MUSCLES = {

    # Chest Subdivisions
    "upper_chest": "Upper Chest",
    "middle_chest": "Middle Chest",
    "lower_chest": "Lower Chest",
    "pectoralis_major": "Chest",
    "pectoralis_minor": "Chest",

    # Back Subdivisions
    "lat_width": "Lats (Back Width)",
    "upper_back": "Upper Back & Mid-Back",
    "lower_back": "Lower Back Strength",
    "latissimus_dorsi": "Lats",
    "trapezius": "Upper Back (Traps)",
    "rhomboids": "Mid-Back",
    "teres_major": "Upper Lats",
    "erector_spinae": "Lower Back",

    # Shoulders
    "front_shoulder": "Front Shoulder",
    "side_shoulder": "Side Shoulder",
    "rear_shoulder": "Rear Shoulder",
    "anterior_deltoid": "Front Shoulder",
    "lateral_deltoid": "Side Shoulder",
    "posterior_deltoid": "Rear Shoulder",

    # Biceps / Arms
    "biceps_outer": "Biceps (Outer Peak)",
    "biceps_inner": "Biceps (Inner Thickness)",
    "biceps_brachii": "Biceps",
    "brachialis": "Outer Bicep / Forearm Tie-in",
    "brachioradialis": "Top Forearm",

    # Triceps
    "triceps_long": "Triceps (Back of Arm)",
    "triceps_outer": "Triceps (Outer Head)",
    "triceps_inner": "Triceps (Inner Head)",
    "triceps_brachii": "Triceps",

    # Forearms
    "forearm_flexors": "Inner Forearm",
    "forearm_extensors": "Outer Forearm",

    # Quadriceps
    "quads": "Thighs (Front Quads)",
    "rectus_femoris": "Thighs (Front Quads)",
    "vastus_lateralis": "Thighs (Outer Quads)",
    "vastus_medialis": "Thighs (Tear-drop Quads)",
    "vastus_intermedius": "Thighs (Inner Quads)",

    # Hamstrings
    "hamstrings": "Hamstrings (Back of Thigh)",
    "biceps_femoris": "Hamstrings (Outer)",
    "semitendinosus": "Hamstrings (Inner)",
    "semimembranosus": "Hamstrings (Deep Inner)",

    # Glutes
    "glutes_main": "Glutes (Main Butt Muscle)",
    "glutes_side": "Side Glutes",
    "gluteus_maximus": "Glutes (Main Butt Muscle)",
    "gluteus_medius": "Side Glutes",
    "gluteus_minimus": "Deep Side Glutes",

    # Calves
    "calves_upper": "Upper Calves",
    "calves_lower": "Lower Calves",
    "gastrocnemius": "Upper Calves",
    "soleus": "Lower Calves",

    # Core
    "abs_front": "Abs (Front Pack)",
    "abs_sides": "Obliques (Side Abs)",
    "rectus_abdominis": "Front Abs",
    "external_oblique": "Side Abs",
    "internal_oblique": "Deep Side Abs",
    "transversus_abdominis": "Core Shield"
}

# ============================================================
# USER-FACING PLAN ANALYSIS TRANSLATIONS (Independent Map)
# ============================================================

SIMPLE_MUSCLE_NAMES = {
    # Chest subdivisions
    "upper_chest": "Upper Chest",
    "middle_chest": "Middle Chest",
    "lower_chest": "Lower Chest",

    # Triceps heads
    "triceps_long": "Triceps (Back of Arm)",
    "triceps_outer": "Triceps (Outer Head)",
    "triceps_inner": "Triceps (Inner Head)",

    # Biceps heads
    "biceps_outer": "Biceps (Outer Peak)",
    "biceps_inner": "Biceps (Inner Thickness)",
    
    # Back subdivisions
    "lat_width": "Lats (Back Width)",
    "upper_back": "Upper Back & Mid-Back",
    "lower_back": "Lower Back Strength",
    
    # Lower Body subdivisions
    "quads": "Thighs (Front Quads)",
    "hamstrings": "Hamstrings (Back of Thigh)",
    "glutes_main": "Glutes (Main Butt Muscle)",
    "glutes_side": "Side Glutes",
    "calves_upper": "Upper Calves",
    "calves_lower": "Lower Calves",
    
    # Core subdivisions
    "abs_front": "Abs (Front Pack)",
    "abs_sides": "Obliques (Side Abs)"
}


# ============================================================
# 2. BODY PARTS
# ============================================================

BODY_PARTS = [

    "Chest",
    "Back",
    "Shoulders",
    "Biceps",
    "Triceps",
    "Forearms",
    "Quadriceps",
    "Hamstrings",
    "Glutes",
    "Calves",
    "Core"

]


# ============================================================
# 3. MOVEMENT PATTERNS
# ============================================================

MOVEMENTS = {

    "horizontal_push": "Horizontal Push",
    "vertical_push": "Vertical Push",

    "horizontal_pull": "Horizontal Pull",
    "vertical_pull": "Vertical Pull",

    "elbow_flexion": "Elbow Flexion",
    "elbow_extension": "Elbow Extension",

    "shoulder_abduction": "Shoulder Abduction",
    "shoulder_extension": "Shoulder Extension",

    "horizontal_adduction": "Horizontal Adduction",
    "horizontal_abduction": "Horizontal Abduction",

    "knee_extension": "Knee Extension",
    "knee_flexion": "Knee Flexion",

    "hip_extension": "Hip Extension",
    "hip_abduction": "Hip Abduction",

    "hip_hinge": "Hip Hinge",

    "ankle_plantarflexion": "Ankle Plantarflexion",

    "trunk_flexion": "Trunk Flexion",

    "anti_extension": "Anti-Extension",
    "anti_lateral_flexion": "Anti-Lateral Flexion",

    "loaded_carry": "Loaded Carry"
}


# ============================================================
# 4. EQUIPMENT
# ============================================================

EQUIPMENT = [

    "Barbell",
    "Dumbbells",
    "Cable",
    "Machine",
    "Bodyweight",
    "EZ-Bar",
    "Kettlebell",
    "Smith Machine",
    "Resistance Band",
    "Landmine",
    "Ab Wheel"

]


# ============================================================
# 5. DAYS OF THE WEEK
# ============================================================

DAYS = [

    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"

]


# ============================================================
# 6. CHECK THAT PART 1 WORKED
# =========================================================

# ============================================================
# FITNESS APP
# PART 2 — EXERCISE KNOWLEDGE DATABASE
# ============================================================


EXERCISES = {

    # ========================================================
    # CHEST
    # ========================================================

    "barbell_bench_press": {
        "id": "barbell_bench_press",
        "name": "Barbell Bench Press",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Barbell",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["anterior_deltoid", "triceps_brachii"],
        "aliases": ["bench press", "barbell press", "flat bench press"],
        "biometric_distribution": {
            "middle_chest": 0.65,
            "lower_chest": 0.20,
            "upper_chest": 0.15
        }
    },

    "dumbbell_bench_press": {
        "id": "dumbbell_bench_press",
        "name": "Dumbbell Bench Press",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Dumbbells",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["anterior_deltoid", "triceps_brachii"],
        "aliases": ["db bench press", "dumbbell press", "flat dumbbell press"],
        "biometric_distribution": {
            "middle_chest": 0.60,
            "lower_chest": 0.25,
            "upper_chest": 0.15
        }
    },

    "incline_barbell_bench_press": {
        "id": "incline_barbell_bench_press",
        "name": "Incline Barbell Bench Press",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Barbell",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["anterior_deltoid", "triceps_brachii"],
        "aliases": ["incline bench press", "incline barbell press"],
        "biometric_distribution": {
            "upper_chest": 0.70,
            "middle_chest": 0.25,
            "lower_chest": 0.05
        }
    },

    "incline_dumbbell_press": {
        "id": "incline_dumbbell_press",
        "name": "Incline Dumbbell Press",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Dumbbells",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["anterior_deltoid", "triceps_brachii"],
        "aliases": ["incline db press", "incline dumbbell bench"],
        "biometric_distribution": {
            "upper_chest": 0.65,
            "middle_chest": 0.30,
            "lower_chest": 0.05
        }
    },

    "decline_barbell_bench_press": {
        "id": "decline_barbell_bench_press",
        "name": "Decline Barbell Bench Press",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Barbell",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["triceps_brachii", "anterior_deltoid"],
        "aliases": ["decline bench press", "decline press"],
        "biometric_distribution": {
            "lower_chest": 0.65,
            "middle_chest": 0.30,
            "upper_chest": 0.05
        }
    },

    "machine_chest_press": {
        "id": "machine_chest_press",
        "name": "Machine Chest Press",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Machine",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["anterior_deltoid", "triceps_brachii"],
        "aliases": ["chest press machine", "machine press"],
        "biometric_distribution": {
            "middle_chest": 0.65,
            "lower_chest": 0.20,
            "upper_chest": 0.15
        }
    },

    "cable_chest_press": {
        "id": "cable_chest_press",
        "name": "Cable Chest Press",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Cable",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["anterior_deltoid", "triceps_brachii"],
        "aliases": ["cable press", "standing cable chest press"],
        "biometric_distribution": {
            "middle_chest": 0.50,
            "lower_chest": 0.35,
            "upper_chest": 0.15
        }
    },

    "pec_deck": {
        "id": "pec_deck",
        "name": "Pec Deck",
        "body_parts": ["Chest"],
        "type": "Isolation",
        "equipment": "Machine",
        "movement": "Horizontal Adduction",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": [],
        "aliases": ["pec fly", "machine chest fly", "chest fly machine"],
        "biometric_distribution": {
            "middle_chest": 0.70,
            "lower_chest": 0.20,
            "upper_chest": 0.10
        }
    },

    "cable_chest_fly": {
        "id": "cable_chest_fly",
        "name": "Cable Chest Fly",
        "body_parts": ["Chest"],
        "type": "Isolation",
        "equipment": "Cable",
        "movement": "Horizontal Adduction",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": [],
        "aliases": ["cable fly", "standing cable fly", "chest cable fly"],
        "biometric_distribution": {
            "lower_chest": 0.50,
            "middle_chest": 0.40,
            "upper_chest": 0.10
        }
    },

    "dumbbell_chest_fly": {
        "id": "dumbbell_chest_fly",
        "name": "Dumbbell Chest Fly",
        "body_parts": ["Chest"],
        "type": "Isolation",
        "equipment": "Dumbbells",
        "movement": "Horizontal Adduction",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": [],
        "aliases": ["db fly", "dumbbell fly"],
        "biometric_distribution": {
            "middle_chest": 0.60,
            "lower_chest": 0.25,
            "upper_chest": 0.15
        }
    },

    "push_up": {
        "id": "push_up",
        "name": "Push-Up",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Bodyweight",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["anterior_deltoid", "triceps_brachii"],
        "aliases": ["pushup", "press up"],
        "biometric_distribution": {
            "middle_chest": 0.55,
            "lower_chest": 0.30,
            "upper_chest": 0.15
        }
    },

    "weighted_push_up": {
        "id": "weighted_push_up",
        "name": "Weighted Push-Up",
        "body_parts": ["Chest"],
        "type": "Compound",
        "equipment": "Bodyweight",
        "movement": "Horizontal Push",
        "primary_muscles": ["pectoralis_major"],
        "secondary_muscles": ["anterior_deltoid", "triceps_brachii"],
        "aliases": ["weighted pushup"],
        "biometric_distribution": {
            "middle_chest": 0.55,
            "lower_chest": 0.30,
            "upper_chest": 0.15
        }
    },

    # ========================================================
    # BACK
    # ========================================================

    "pull_up": {
        "id": "pull_up",
        "name": "Pull-Up",
        "body_parts": ["Back"],
        "type": "Compound",
        "equipment": "Bodyweight",
        "movement": "Vertical Pull",
        "primary_muscles": ["latissimus_dorsi"],
        "secondary_muscles": ["biceps_brachii", "brachialis"],
        "aliases": ["pullup", "wide grip pullup"],
        "biometric_distribution": {
            "lat_width": 0.75,
            "upper_back": 0.25
        }
    },

    "chin_up": {
        "id": "chin_up",
        "name": "Chin-Up",
        "body_parts": ["Back", "Biceps"],
        "type": "Compound",
        "equipment": "Bodyweight",
        "movement": "Vertical Pull",
        "primary_muscles": ["latissimus_dorsi", "biceps_brachii"],
        "secondary_muscles": ["brachialis", "brachioradialis"],
        "aliases": ["chinup", "underhand pullup"],
        "biometric_distribution": {
            "lat_width": 0.60,
            "biceps_inner": 0.40
        }
    },

    "lat_pulldown": {
        "id": "lat_pulldown",
        "name": "Lat Pulldown",
        "body_parts": ["Back"],
        "type": "Compound",
        "equipment": "Cable",
        "movement": "Vertical Pull",
        "primary_muscles": ["latissimus_dorsi"],
        "secondary_muscles": ["biceps_brachii", "brachialis"],
        "aliases": ["pulldown", "lat pull down"],
        "biometric_distribution": {
            "lat_width": 0.80,
            "upper_back": 0.20
        }
    },

    "barbell_row": {
        "id": "barbell_row",
        "name": "Barbell Row",
        "body_parts": ["Back"],
        "type": "Compound",
        "equipment": "Barbell",
        "movement": "Horizontal Pull",
        "primary_muscles": ["latissimus_dorsi", "trapezius", "rhomboids"],
        "secondary_muscles": ["posterior_deltoid", "biceps_brachii", "erector_spinae"],
        "aliases": ["bent over row", "barbell bent over row"],
        "biometric_distribution": {
            "upper_back": 0.55,
            "lat_width": 0.30,
            "lower_back": 0.15
        }
    },

    "dumbbell_row": {
        "id": "dumbbell_row",
        "name": "Dumbbell Row",
        "body_parts": ["Back"],
        "type": "Compound",
        "equipment": "Dumbbells",
        "movement": "Horizontal Pull",
        "primary_muscles": ["latissimus_dorsi", "rhomboids"],
        "secondary_muscles": ["posterior_deltoid", "biceps_brachii"],
        "aliases": ["db row", "one arm dumbbell row"],
        "biometric_distribution": {
            "lat_width": 0.55,
            "upper_back": 0.45
        }
    },

    "seated_cable_row": {
        "id": "seated_cable_row",
        "name": "Seated Cable Row",
        "body_parts": ["Back"],
        "type": "Compound",
        "equipment": "Cable",
        "movement": "Horizontal Pull",
        "primary_muscles": ["latissimus_dorsi", "rhomboids"],
"secondary_muscles": ["trapezius", "posterior_deltoid", "biceps_brachii"],"aliases": ["cable row", "seated row"],"biometric_distribution": {"upper_back": 0.60,"lat_width": 0.40}},


    "chest_supported_row": {"id": "chest_supported_row","name": "Chest-Supported Row","body_parts": ["Back"],"type": "Compound","equipment": "Machine","movement": "Horizontal Pull","primary_muscles": ["rhomboids", "trapezius", "latissimus_dorsi"],"secondary_muscles": ["posterior_deltoid", "biceps_brachii"],"aliases": ["chest supported machine row"],"biometric_distribution": {"upper_back": 0.70,"lat_width": 0.30}},"straight_arm_pulldown": {"id": "straight_arm_pulldown","name": "Straight-Arm Pulldown","body_parts": ["Back"],"type": "Isolation","equipment": "Cable","movement": "Shoulder Extension","primary_muscles": ["latissimus_dorsi"],"secondary_muscles": ["teres_major"],"aliases": ["straight arm pulldown", "cable pullover"],"biometric_distribution": {"lat_width": 0.90,"upper_back": 0.10}},"barbell_shrug": {"id": "barbell_shrug","name": "Barbell Shrug","body_parts": ["Back"],"type": "Isolation","equipment": "Barbell","movement": "Loaded Carry","primary_muscles": ["trapezius"],"secondary_muscles": [],"aliases": ["shrugs", "barbell shrugs"],"biometric_distribution": {"upper_back": 1.00  # Completely targets upper traps/neck line
    }},


    # ========================================================
    # SHOULDERS
    # ========================================================

"barbell_overhead_press": {"id": "barbell_overhead_press","name": "Barbell Overhead Press","body_parts": ["Shoulders"],"type": "Compound","equipment": "Barbell","movement": "Vertical Push","primary_muscles": ["anterior_deltoid", "lateral_deltoid"],"secondary_muscles": ["triceps_brachii"],"aliases": ["ohp", "military press", "barbell shoulder press"],"biometric_distribution": {"front_shoulder": 0.70,"side_shoulder": 0.30}},"dumbbell_shoulder_press": {"id": "dumbbell_shoulder_press","name": "Dumbbell Shoulder Press","body_parts": ["Shoulders"],"type": "Compound","equipment": "Dumbbells","movement": "Vertical Push","primary_muscles": ["anterior_deltoid", "lateral_deltoid"],"secondary_muscles": ["triceps_brachii"],"aliases": ["db shoulder press", "dumbbell overhead press"],"biometric_distribution": {"front_shoulder": 0.65,"side_shoulder": 0.35}},"machine_shoulder_press": {"id": "machine_shoulder_press","name": "Machine Shoulder Press","body_parts": ["Shoulders"],"type": "Compound","equipment": "Machine","movement": "Vertical Push","primary_muscles": ["anterior_deltoid", "lateral_deltoid"],"secondary_muscles": ["triceps_brachii"],"aliases": ["shoulder press machine"],"biometric_distribution": {"front_shoulder": 0.75,"side_shoulder": 0.25}},"dumbbell_lateral_raise": {"id": "dumbbell_lateral_raise","name": "Dumbbell Lateral Raise","body_parts": ["Shoulders"],"type": "Isolation","equipment": "Dumbbells","movement": "Shoulder Abduction","primary_muscles": ["lateral_deltoid"],"secondary_muscles": [],"aliases": ["lateral raise", "side raise", "db lateral raise"],"biometric_distribution": {"side_shoulder": 1.00}},"cable_lateral_raise": {"id": "cable_lateral_raise","name": "Cable Lateral Raise","body_parts": ["Shoulders"],"type": "Isolation","equipment": "Cable","movement": "Shoulder Abduction","primary_muscles": ["lateral_deltoid"],"secondary_muscles": [],"aliases": ["cable side raise"],"biometric_distribution": {"side_shoulder": 1.00}},"reverse_pec_deck": {"id": "reverse_pec_deck","name": "Reverse Pec Deck","body_parts": ["Shoulders", "Back"],"type": "Isolation","equipment": "Machine","movement": "Horizontal Abduction","primary_muscles": ["posterior_deltoid"],"secondary_muscles": ["trapezius", "rhomboids"],"aliases": ["rear delt machine", "reverse fly machine"],"biometric_distribution": {"rear_shoulder": 0.70,"upper_back": 0.30}},"dumbbell_rear_delt_fly": {"id": "dumbbell_rear_delt_fly","name": "Dumbbell Rear Delt Fly","body_parts": ["Shoulders"],"type": "Isolation","equipment": "Dumbbells","movement": "Horizontal Abduction","primary_muscles": ["posterior_deltoid"],"secondary_muscles": ["rhomboids", "trapezius"],"aliases": ["rear delt fly", "reverse dumbbell fly"],"biometric_distribution": {"rear_shoulder": 0.75,"upper_back": 0.25}},


    # ========================================================
    # BICEPS
    # ========================================================
"barbell_curl": {"id": "barbell_curl","name": "Barbell Curl","body_parts": ["Biceps"],"type": "Isolation","equipment": "Barbell","movement": "Elbow Flexion","primary_muscles": ["biceps_brachii"],"secondary_muscles": ["brachialis", "brachioradialis"],"aliases": ["barbell biceps curl"],"biometric_distribution": {"biceps_inner": 0.50,"biceps_outer": 0.50}},"ez_bar_curl": {"id": "ez_bar_curl","name": "EZ-Bar Curl","body_parts": ["Biceps"],"type": "Isolation","equipment": "EZ-Bar","movement": "Elbow Flexion","primary_muscles": ["biceps_brachii"],"secondary_muscles": ["brachialis", "brachioradialis"],"aliases": ["ez curl", "ez bar biceps curl"],"biometric_distribution": {"biceps_outer": 0.60,"biceps_inner": 0.40}},"dumbbell_curl": {"id": "dumbbell_curl","name": "Dumbbell Curl","body_parts": ["Biceps"],"type": "Isolation","equipment": "Dumbbells","movement": "Elbow Flexion","primary_muscles": ["biceps_brachii"],"secondary_muscles": ["brachialis", "brachioradialis"],"aliases": ["db curl", "dumbbell bicep curl"],"biometric_distribution": {"biceps_inner": 0.50,"biceps_outer": 0.50}},"hammer_curl": {"id": "hammer_curl","name": "Hammer Curl","body_parts": ["Biceps"],"type": "Isolation","equipment": "Dumbbells","movement": "Elbow Flexion","primary_muscles": ["brachialis", "brachioradialis"],"secondary_muscles": ["biceps_brachii"],"aliases": ["db hammer curl", "neutral grip curl"],"biometric_distribution": {"biceps_outer": 0.80,  # Shifting high strain onto the brachialis/outer ridge line
"biceps_inner": 0.20}},"incline_dumbbell_curl": {"id": "incline_dumbbell_curl","name": "Incline Dumbbell Curl","body_parts": ["Biceps"],"type": "Isolation","equipment": "Dumbbells","movement": "Elbow Flexion","primary_muscles": ["biceps_brachii"],"secondary_muscles": ["brachialis"],"aliases": ["incline db curl"],"biometric_distribution": {"biceps_outer": 0.75,  # Maximises long head stretch peak
"biceps_inner": 0.25}},"preacher_curl": {"id": "preacher_curl","name": "Preacher Curl","body_parts": ["Biceps"],"type": "Isolation","equipment": "Machine","movement": "Elbow Flexion","primary_muscles": ["biceps_brachii"],"secondary_muscles": ["brachialis"],"aliases": ["preacher bicep curl"],"biometric_distribution": {"biceps_inner": 0.75,  # Short head absolute thickness biomechanics focus
"biceps_outer": 0.25}},"cable_curl": {"id": "cable_curl","name": "Cable Curl","body_parts": ["Biceps"],"type": "Isolation","equipment": "Cable","movement": "Elbow Flexion","primary_muscles": ["biceps_brachii"],"secondary_muscles": ["brachialis", "brachioradialis"],"aliases": ["standing cable curl"],"biometric_distribution": {"biceps_inner": 0.50,"biceps_outer": 0.50}},



    # ========================================================
    # TRICEPS
    # ========================================================
"triceps_pushdown": {"id": "triceps_pushdown","name": "Triceps Pushdown","body_parts": ["Triceps"],"type": "Isolation","equipment": "Cable","movement": "Elbow Extension","primary_muscles": ["triceps_brachii"],"secondary_muscles": [],"aliases": ["tricep pushdown", "cable pushdown", "rope pushdown"],"biometric_distribution": {"triceps_outer": 0.50,"triceps_inner": 0.30,"triceps_long": 0.20}},"overhead_cable_triceps_extension": {"id": "overhead_cable_triceps_extension","name": "Overhead Cable Triceps Extension","body_parts": ["Triceps"],"type": "Isolation","equipment": "Cable","movement": "Elbow Extension","primary_muscles": ["triceps_brachii"],"secondary_muscles": [],"aliases": ["overhead cable extension"],"biometric_distribution": {"triceps_long": 0.70,"triceps_outer": 0.15,"triceps_inner": 0.15}},"skull_crusher": {"id": "skull_crusher","name": "Skull Crusher","body_parts": ["Triceps"],"type": "Isolation","equipment": "EZ-Bar","movement": "Elbow Extension","primary_muscles": ["triceps_brachii"],"secondary_muscles": [],"aliases": ["lying triceps extension", "ez bar skull crusher"],"biometric_distribution": {"triceps_long": 0.55,"triceps_outer": 0.25,"triceps_inner": 0.20}},"close_grip_bench_press": {"id": "close_grip_bench_press","name": "Close-Grip Bench Press","body_parts": ["Triceps", "Chest"],"type": "compound","equipment": "Barbell","movement": "Horizontal Push","primary_muscles": ["triceps_brachii"],"secondary_muscles": ["pectoralis_major", "anterior_deltoid"],"aliases": ["close grip bench", "close grip press"],"biometric_distribution": {"triceps_outer": 0.40,"triceps_inner": 0.40,"middle_chest": 0.20}},

#=================================
           #QUADRICEPS
#=====≠===============================
"back_squat": {"id": "back_squat","name": "Back Squat","body_parts": ["Quadriceps", "Glutes"],"type": "Compound","equipment": "Barbell","movement": "Knee + Hip Extension","primary_muscles": ["rectus_femoris", "vastus_lateralis", "vastus_medialis", "vastus_intermedius"],"secondary_muscles": ["gluteus_maximus", "erector_spinae"],"aliases": ["barbell squat", "squat"],"biometric_distribution": {"quads": 0.60,"glutes_main": 0.40}},"front_squat": {"id": "front_squat","name": "Front Squat","body_parts": ["Quadriceps", "Glutes"],"type": "Compound","equipment": "Barbell","movement": "Knee + Hip Extension","primary_muscles": ["rectus_femoris", "vastus_lateralis", "vastus_medialis", "vastus_intermedius"],"secondary_muscles": ["gluteus_maximus"],"aliases": ["barbell front_squat"],"biometric_distribution": {"quads": 0.75,"glutes_main": 0.25}},"leg_press": {"id": "leg_press","name": "Leg Press","body_parts": ["Quadriceps", "Glutes"],"type": "Compound","equipment": "Machine","movement": "Knee + Hip Extension","primary_muscles": ["rectus_femoris", "vastus_lateralis", "vastus_medialis", "vastus_intermedius"],"secondary_muscles": ["gluteus_maximus"],"aliases": ["leg press machine"],"biometric_distribution": {"quads": 0.70,"glutes_main": 0.30}},"hack_squat": {"id": "hack_squat","name": "Hack Squat","body_parts": ["Quadriceps", "Glutes"],"type": "Compound","equipment": "Machine","movement": "Knee + Hip Extension","primary_muscles": ["rectus_femoris", "vastus_lateralis", "vastus_medialis", "vastus_intermedius"],"secondary_muscles": ["gluteus_maximus"],"aliases": ["hack squat machine"],"biometric_distribution": {"quads": 0.80,"glutes_main": 0.20}},"leg_extension": {"id": "leg_extension","name": "Leg Extension","body_parts": ["Quadriceps"],"type": "Isolation","equipment": "Machine","movement": "Knee Extension","primary_muscles": ["rectus_femoris", "vastus_lateralis", "vastus_medialis", "vastus_intermedius"],"secondary_muscles": [],"aliases": ["quad extension"],"biometric_distribution": {"quads": 1.00}},"bulgarian_split_squat": {"id": "bulgarian_split_squat","name": "Bulgarian Split Squat","body_parts": ["Quadriceps", "Glutes"],"type": "Compound","equipment": "Dumbbells","movement": "Knee + Hip Extension","primary_muscles": ["rectus_femoris", "vastus_lateralis", "vastus_medialis", "vastus_intermedius"],"secondary_muscles": ["gluteus_maximus"],"aliases": ["rear foot elevated split squat", "split squat"],"biometric_distribution": {"glutes_main": 0.50,"quads": 0.50}},
#====================================
           #HAMSTRING
#====================================
"romanian_deadlift": {"id": "romanian_deadlift","name": "Romanian Deadlift","body_parts": ["Hamstrings", "Glutes"],"type": "Compound","equipment": "Barbell","movement": "Hip Hinge","primary_muscles": ["biceps_femoris", "semitendinosus", "semimembranosus"],"secondary_muscles": ["gluteus_maximus", "erector_spinae"],"aliases": ["rdl", "barbell rdl"],"biometric_distribution": {"hamstrings": 0.60,"glutes_main": 0.30,"lower_back": 0.10}},"dumbbell_romanian_deadlift": {"id": "dumbbell_romanian_deadlift","name": "Dumbbell Romanian Deadlift","body_parts": ["Hamstrings", "Glutes"],"type": "Compound","equipment": "Dumbbells","movement": "Hip Hinge","primary_muscles": ["biceps_femoris", "semitendinosus", "semimembranosus"],"secondary_muscles": ["gluteus_maximus"],"aliases": ["db rdl", "dumbbell rdl"],"biometric_distribution": {"hamstrings": 0.65,"glutes_main": 0.35}},"lying_leg_curl": {"id": "lying_leg_curl","name": "Lying Leg Curl","body_parts": ["Hamstrings"],"type": "Isolation","equipment": "Machine","movement": "Knee Flexion","primary_muscles": ["biceps_femoris", "semitendinosus", "semimembranosus"],"secondary_muscles": [],"aliases": ["leg curl", "lying hamstring curl"],"biometric_distribution": {"hamstrings": 1.00}},"seated_leg_curl": {"id": "seated_leg_curl","name": "Seated Leg Curl","body_parts": ["Hamstrings"],"type": "Isolation","equipment": "Machine","movement": "Knee Flexion","primary_muscles": ["biceps_femoris", "semitendinosus", "semimembranosus"],"secondary_muscles": [],"aliases": ["seated hamstring curl"],"biometric_distribution": {"hamstrings": 1.00}},
#=====================
#     GLUTES  
#======================
"barbell_hip_thrust": {"id": "barbell_hip_thrust","name": "Barbell Hip Thrust","body_parts": ["Glutes"],"type": "Compound","equipment": "Barbell","movement": "Hip Extension","primary_muscles": ["gluteus_maximus"],"secondary_muscles": ["biceps_femoris", "semitendinosus", "semimembranosus"],"aliases": ["hip thrust"],"biometric_distribution": {"glutes_main": 0.80,"hamstrings": 0.20}},"glute_bridge": {"id": "glute_bridge","name": "Glute Bridge","body_parts": ["Glutes"],"type": "Compound","equipment": "Bodyweight","movement": "Hip Extension","primary_muscles": ["gluteus_maximus"],"secondary_muscles": [],"aliases": ["bodyweight glute bridge"],"biometric_distribution": {"glutes_main": 1.00}},"cable_kickback": {"id": "cable_kickback","name": "Cable Glute Kickback","body_parts": ["Glutes"],"type": "Isolation","equipment": "Cable","movement": "Hip Extension","primary_muscles": ["gluteus_maximus"],"secondary_muscles": [],"aliases": ["cable kickback", "glute kickback"],"biometric_distribution": {"glutes_main": 1.00}},"hip_abduction_machine": {"id": "hip_abduction_machine","name": "Hip Abduction Machine","body_parts": ["Glutes"],"type": "Isolation","equipment": "Machine","movement": "Hip Abduction","primary_muscles": ["gluteus_medius", "gluteus_minimus"],"secondary_muscles": [],"aliases": ["abduction machine", "hip abduction"],"biometric_distribution": {"glutes_side": 1.00}},
#===========
#CALVES
#====≠======
"standing_calf_raise": {"id": "standing_calf_raise","name": "Standing Calf Raise","body_parts": ["Calves"],"type": "Isolation","equipment": "Machine","movement": "Ankle Plantarflexion","primary_muscles": ["gastrocnemius"],"secondary_muscles": ["soleus"],"aliases": ["calf raise"],"biometric_distribution": {"calves_upper": 0.75,"calves_lower": 0.25}},"seated_calf_raise": {"id": "seated_calf_raise","name": "Seated Calf Raise","body_parts": ["Calves"],"type": "Isolation","equipment": "Machine","movement": "Ankle Plantarflexion","primary_muscles": ["soleus"],"secondary_muscles": ["gastrocnemius"],"aliases": ["seated calf raise"],"biometric_distribution": {"calves_lower": 0.80,"calves_upper": 0.20}},
#====≠==========
#     CORE
#===============
"cable_crunch": {"id": "cable_crunch","name": "Cable Crunch","body_parts": ["Core"],"type": "Isolation","equipment": "Cable","movement": "Trunk Flexion","primary_muscles": ["rectus_abdominis"],"secondary_muscles": ["external_oblique", "internal_oblique"],"aliases": ["kneeling cable crunch"],"biometric_distribution": {"abs_front": 0.80,"abs_sides": 0.20}},"crunch": {"id": "crunch","name": "Crunch","body_parts": ["Core"],"type": "Isolation","equipment": "Bodyweight","movement": "Trunk Flexion","primary_muscles": ["rectus_abdominis"],"secondary_muscles": [],"aliases": ["ab crunch"],"biometric_distribution": {"abs_front": 1.00}},"hanging_leg_raise": {"id": "hanging_leg_raise","name": "Hanging Leg Raise","body_parts": ["Core"],"type": "Compound","equipment": "Bodyweight","movement": "Hip Flexion","primary_muscles": ["rectus_abdominis"],"secondary_muscles": [],"aliases": ["hanging leg raises"],"biometric_distribution": {"abs_front": 1.00  # High lower abs emphasis
}},"ab_wheel_rollout": {"id": "ab_wheel_rollout","name": "Ab Wheel Rollout","body_parts": ["Core"],"type": "Compound","equipment": "Ab Wheel","movement": "Anti-Extension","primary_muscles": ["rectus_abdominis", "transversus_abdominis"],"secondary_muscles": ["external_oblique", "internal_oblique"],"aliases": ["ab rollout", "wheel rollout"],"biometric_distribution": {"abs_front": 0.70,"abs_sides": 0.30}},"plank": {"id": "plank","name": "Plank","body_parts": ["Core"],"type": "Isometric","equipment": "Bodyweight","movement": "Anti-Extension","primary_muscles": ["transversus_abdominis", "rectus_abdominis"],"secondary_muscles": ["external_oblique", "internal_oblique"],"aliases": ["front plank"],"biometric_distribution": {"abs_front": 0.60,"abs_sides": 0.40}}}

# ============================================================
# FITNESS APP
# PART 3 — EXERCISE SEARCH & SELECTION
# ============================================================


# ============================================================
# 1. SEARCH EXERCISES
# ============================================================

def search_exercises(search_text):

    search_text = search_text.lower().strip()

    results = []

    for exercise_id, exercise in EXERCISES.items():

        name = exercise["name"].lower()

        aliases = [
            alias.lower()
            for alias in exercise["aliases"]
        ]

        body_parts = [
            part.lower()
            for part in exercise["body_parts"]
        ]

        # Search name
        if search_text in name:
            results.append(exercise_id)
            continue

        # Search aliases
        if any(search_text in alias for alias in aliases):
            results.append(exercise_id)
            continue

        # Search body part
        if any(search_text in part for part in body_parts):
            results.append(exercise_id)
            continue

    return results


# ============================================================
# 2. DISPLAY EXERCISE DETAILS
# ============================================================

def show_exercise(exercise_id):

    exercise = EXERCISES[exercise_id]

    print("\n==========================================")
    print(exercise["name"])
    print("==========================================")

    print(
        "Body Part:",
        ", ".join(exercise["body_parts"])
    )

    print(
        "Type:",
        exercise["type"]
    )

    print(
        "Equipment:",
        exercise["equipment"]
    )

    print(
        "Movement:",
        exercise["movement"]
    )

    print("\nPrimary Muscles:")

    for muscle in exercise["primary_muscles"]:

        if muscle in MUSCLES:
            print(
                " -",
                MUSCLES[muscle]
            )

    print("\nSecondary Muscles:")

    if exercise["secondary_muscles"]:

        for muscle in exercise["secondary_muscles"]:

            if muscle in MUSCLES:
                print(
                    " -",
                    MUSCLES[muscle]
                )

    else:

        print(" - None listed")


# ============================================================
# 3. SEARCH + SELECT ONE EXERCISE
# ============================================================

def select_exercise():

    search_text = input(
        "\nSearch exercise: "
    )

    results = search_exercises(search_text)

    if not results:

        print(
            "\nNo exercises found."
        )

        return None


    print("\nMatching Exercises:")

    for number, exercise_id in enumerate(
        results,
        start=1
    ):

        print(
            f"{number}. {EXERCISES[exercise_id]['name']}"
        )


    while True:

        choice = input(
            "\nSelect exercise number: "
        )

        try:

            choice = int(choice)

            if 1 <= choice <= len(results):

                selected_id = results[choice - 1]

                show_exercise(selected_id)

                return selected_id

            else:

                print(
                    "Please enter a valid number."
                )

        except ValueError:

            print(
                "Please enter a number."
            )
    # ============================================================
# FITNESS APP
# PART 4 — 7-DAY WORKOUT PLAN BUILDER
# ============================================================


# ============================================================
# 1. WORKOUT PLAN STORAGE
# ============================================================

WORKOUT_PLAN = {

    day: {
        "body_parts": [],
        "exercises": []
    }

    for day in DAYS
}


# ============================================================
# 2. SELECT BODY PARTS
# ============================================================

def select_body_parts():

    print("\n==========================================")
    print("SELECT BODY PARTS")
    print("==========================================")

    for number, body_part in enumerate(
        BODY_PARTS,
        start=1
    ):

        print(
            f"{number}. {body_part}"
        )


    print(
        "\nEnter numbers separated by commas."
    )

    print(
        "Example: 1,4"
    )


    while True:

        selection = input(
            "\nYour selection: "
        ).strip()


        try:

            numbers = [
                int(number.strip())
                for number in selection.split(",")
            ]


            selected_parts = []


            for number in numbers:

                if 1 <= number <= len(BODY_PARTS):

                    body_part = BODY_PARTS[number - 1]

                    if body_part not in selected_parts:

                        selected_parts.append(
                            body_part
                        )

                else:

                    print(
                        f"Invalid number: {number}"
                    )

                    selected_parts = []

                    break


            if selected_parts:

                return selected_parts


        except ValueError:

            print(
                "Please enter numbers only."
            )


# ============================================================
# 3. ADD EXERCISE TO DAY
# ============================================================

def add_exercise_to_day(day):

    print("\n==========================================")
    print(f"ADD EXERCISE — {day}")
    print("==========================================")


    selected_exercise = select_exercise()


    if selected_exercise is None:

        return False


    # --------------------------------------------------------
    # SELECTED EXERCISE IS ALREADY THE EXERCISE DICTIONARY
    # --------------------------------------------------------

    exercise = selected_exercise


    # --------------------------------------------------------
    # GET EXERCISE ID
    # --------------------------------------------------------

    selected_id = exercise.get(
        "id",
        exercise.get("exercise_id")
    )


    # --------------------------------------------------------
    # CHECK WHETHER EXERCISE MATCHES SELECTED BODY PART
    # --------------------------------------------------------

    selected_body_parts = (
        WORKOUT_PLAN[day]["body_parts"]
    )


    matching_parts = [

        part

        for part in exercise["body_parts"]

        if part in selected_body_parts

    ]


    if not matching_parts:

        print("\n------------------------------------------")
        print("WARNING:")

        print(
            f"{exercise['name']} is not directly "
            f"associated with the selected body parts."
        )

        print("------------------------------------------")


        continue_anyway = input(
            "Add it anyway? (yes/no): "
        ).lower().strip()


        if continue_anyway != "yes":

            print(
                "\nExercise not added."
            )

            return False


    # --------------------------------------------------------
    # ENTER PLANNED SETS
    # --------------------------------------------------------

    while True:

        try:

            sets = int(
                input(
                    "\nNumber of sets: "
                )
            )


            if sets > 0:

                break


            print(
                "Sets must be greater than 0."
            )


        except ValueError:

            print(
                "Please enter a whole number."
            )


    # --------------------------------------------------------
    # ENTER REPS
    # --------------------------------------------------------

    while True:

        try:

            reps = int(
                input(
                    "Target reps per set: "
                )
            )


            if reps >= 0:

                break


            print(
                "Reps cannot be negative."
            )


        except ValueError:

            print(
                "Please enter a whole number."
            )


    # --------------------------------------------------------
    # ENTER STARTING / PLANNED WEIGHT
    # --------------------------------------------------------

    while True:

        try:

            weight = float(
                input(
                    "Starting weight (0 if beginner): "
                )
            )


            if weight >= 0:

                break


            print(
                "Weight cannot be negative."
            )


        except ValueError:

            print(
                "Please enter a valid number."
            )


    # --------------------------------------------------------
    # SAVE EXERCISE
    # --------------------------------------------------------

    exercise_data = {

        "exercise_id": selected_id,

        "exercise_name": exercise["name"],

        "sets": sets,

        "reps": reps,

        "weight": weight

    }


    WORKOUT_PLAN[day]["exercises"].append(
        exercise_data
    )


    print("\n==========================================")

    print(
        f"{exercise['name']} added to {day}."
    )

    print(
        f"Sets: {sets}"
    )

    print(
        f"Reps: {reps}"
    )

    print(
        f"Weight: {weight}"
    )

    print("==========================================")


    return True


# ============================================================
# 4. SHOW DAY PLAN
# ============================================================

def show_day_plan(day):

    plan = WORKOUT_PLAN[day]


    print("\n")
    print("==========================================")
    print(f"{day.upper()} WORKOUT PLAN")
    print("==========================================")


    if not plan["body_parts"]:

        print("Body Parts: None")

    else:

        print(
            "Body Parts:",
            ", ".join(plan["body_parts"])
        )


    print("\nExercises:")


    if not plan["exercises"]:

        print("No exercises added.")

        return


    for number, exercise in enumerate(
        plan["exercises"],
        start=1
    ):

        print(
            f"\n{number}. {exercise['exercise_name']}"
        )

        print(
            f"   Sets: {exercise['sets']}"
        )

        print(
            f"   Reps: {exercise['reps']}"
        )

        print(
            f"   Weight: {exercise['weight']}"
        )

    print("\n==========================================")
#---------NEW
import sqlite3

def get_database_connection():
    connection = sqlite3.connect("fitness_app.db")
    connection.row_factory = sqlite3.Row
    return connection

#---------NEW

def save_day_plan(day):

    connection = get_database_connection()

    cursor = connection.cursor()


    # --------------------------------------------------------
    # REMOVE OLD PLAN FOR THIS DAY
    # --------------------------------------------------------

    cursor.execute("""

        SELECT id

        FROM workout_plans

        WHERE day = ?

    """, (day,))


    old_plan = cursor.fetchone()


    if old_plan:

        old_plan_id = old_plan["id"]


        cursor.execute("""

            DELETE FROM plan_body_parts

            WHERE plan_id = ?

        """, (old_plan_id,))


        cursor.execute("""

            DELETE FROM planned_exercises

            WHERE plan_id = ?

        """, (old_plan_id,))


        cursor.execute("""

            DELETE FROM workout_plans

            WHERE id = ?

        """, (old_plan_id,))


    # --------------------------------------------------------
    # CREATE NEW PLAN
    # --------------------------------------------------------

    cursor.execute("""

        INSERT INTO workout_plans (day)

        VALUES (?)

    """, (day,))


    plan_id = cursor.lastrowid


    # --------------------------------------------------------
    # SAVE BODY PARTS
    # --------------------------------------------------------

    for body_part in WORKOUT_PLAN[day]["body_parts"]:

        cursor.execute("""

            INSERT INTO plan_body_parts (

                plan_id,
                body_part

            )

            VALUES (?, ?)

        """, (

            plan_id,
            body_part

        ))


    # --------------------------------------------------------
    # SAVE PLANNED EXERCISES
    # --------------------------------------------------------

    for exercise in WORKOUT_PLAN[day]["exercises"]:

        cursor.execute("""

            INSERT INTO planned_exercises (

                plan_id,
                exercise_id,
                exercise_name,
                sets,
                reps,
                weight

            )

            VALUES (?, ?, ?, ?, ?, ?)

        """, (

            plan_id,

            exercise["exercise_id"],

            exercise["exercise_name"],

            exercise["sets"],

            exercise["reps"],

            exercise["weight"]

        ))


    connection.commit()

    connection.close()


    print(
        f"\n{day} plan saved successfully."
    )

# ============================================================
# 5. BUILD ONE DAY
# ============================================================

def build_day(day):

    print("\n")
    print("##########################################")
    print(f"BUILDING WORKOUT — {day.upper()}")
    print("##########################################")


    # --------------------------------------------------------
    # SELECT BODY PARTS
    # --------------------------------------------------------

    body_parts = select_body_parts()


    WORKOUT_PLAN[day]["body_parts"] = body_parts


    print("\nSelected body parts:")

    for part in body_parts:

        print(
            " -",
            part
        )


    # --------------------------------------------------------
    # ADD EXERCISES
    # --------------------------------------------------------

    while True:

        add_exercise_to_day(day)


        another = input(
            "\nAdd another exercise? (yes/no): "
        ).lower().strip()


        if another != "yes":

            break


    # --------------------------------------------------------
    # SHOW COMPLETED DAY
    # --------------------------------------------------------

    show_day_plan(day)
    
    save_day_plan(day)


# ============================================================
# 6. SELECT DAY
# ============================================================

def select_day():

    print("\n==========================================")
    print("SELECT WORKOUT DAY")
    print("==========================================")


    for number, day in enumerate(
        DAYS,
        start=1
    ):

        print(
            f"{number}. {day}"
        )


    print("8. Back")


    while True:

        try:

            choice = int(
                input(
                    "\nChoose day number: "
                )
            )


            # ----------------------------------------------
            # BACK
            # ----------------------------------------------

            if choice == 8:

                return None


            # ----------------------------------------------
            # SELECT DAY
            # ----------------------------------------------

            if 1 <= choice <= len(DAYS):

                return DAYS[choice - 1]


            print(
                "Please select a valid option."
            )


        except ValueError:

            print(
                "Please enter a number."
            )
#==================================
#ANALYSE PLANNED WORKOUT ROUTINE
#===≠==============================
def analyze_planned_workout_routine():
    # --- GLOBAL SYSTEM MAPS & THRESHOLDS ---
    MEV = 4.0                 # Minimum Effective Volume per week
    MRV = 20.0                # Maximum Recoverable Volume threshold
    SESSION_MAX_SETS = 6.0    # Junk volume ceiling per muscle per day
    MAX_SESSION_DURATION_SETS = 22 # Pillar 9: Upper limit for set quality collapse
    muscle_groups_data = {
        "Chest": ["upper_chest", "middle_chest", "lower_chest"],
        "Back": ["lat_width", "upper_back", "lower_back"],
        "Shoulders": ["front_shoulder", "side_shoulder", "rear_shoulder"],
        "Arms": ["biceps_outer", "biceps_inner", "triceps_long", "triceps_outer", "triceps_inner"],
        "Legs": ["quads", "hamstrings", "glutes_main", "glutes_side", "calves_upper", "calves_lower"],
        "Core": ["abs_front", "abs_sides"],
    }
    # Custom advice triggers for completely ignored body structures
    ignored_group_advice = {
        "Chest": "🔴 No chest exercises found! If you want a complete, balanced physique, add pressing variants or flyes.",
        "Back": "🔴 No back exercises found! Ignoring the back causes terrible posture and leaves your pull muscles underdeveloped.",
        "Shoulders": "🔴 No shoulder exercises found! A complete upper body requires side raises and pressing variants to build strength.",
        "Arms": "🔴 No arm exercises found! Consider adding direct bicep curls and tricep pushdowns to stimulate upper body mass.",
        "Legs": "🔴 No leg exercises found! Skipping quads, hamstrings, and calves limits overall structural growth and metabolism.",
        "Core": "🔴 No core exercises found! If you want torso stability and a strong midsection, add front ab work or side obliques.",
    }

    # Trackers for Multi-Session Scoring
    weekly_subdivision_volume = {}  
    muscle_frequency = {}           
    push_pull_balance = {"push": 0, "pull": 0}
    quad_hip_balance = {"quad_dominant": 0, "hip_dominant": 0}
    
    # Pillar 10: Track exact movement patterns utilized per day to catch redundancy
    daily_movement_redundancy = {} 
    
    session_warnings = []
    has_exercises = False

    # Mapping sub-keys back to their simple parent groups for broad data aggregations
    broad_group_mapping = {
        "upper_chest": "Chest", "middle_chest": "Chest", "lower_chest": "Chest",
        "triceps_long": "Triceps", "triceps_outer": "Triceps", "triceps_inner": "Triceps",
        "biceps_outer": "Biceps", "biceps_inner": "Biceps",
        "lat_width": "Back", "upper_back": "Back", "lower_back": "Back",
        "front_shoulder": "Shoulders", "side_shoulder": "Shoulders", "rear_shoulder": "Shoulders",
        "quads": "Legs (Quads)", "hamstrings": "Legs (Hamstrings)", 
        "glutes_main": "Legs (Glutes)", "glutes_side": "Legs (Glutes)",
        "calves_upper": "Legs (Calves)", "calves_lower": "Legs (Calves)",
        "abs_front": "Core", "abs_sides": "Core"
    }

    # Initialize master calculation storage maps
    weekly_subdivision_volume = {k: 0.0 for bucket in muscle_groups_data.values() for k in bucket}
    muscle_frequency = {group: 0 for group in muscle_groups_data}
    push_pull_balance = {"push": 0.0, "pull": 0.0}
    quad_hip_balance = {"quad_dominant": 0.0, "hip_dominant": 0.0}
    daily_movement_redundancy = {day: {} for day in DAYS}
    session_warnings = []
    has_exercises = False

    # 1. RUN COMPILATION LOOPS OVER THE ENTIRE WORKOUT_PLAN WEEK
    for day in DAYS:
        day_plan = WORKOUT_PLAN.get(day, {})
        planned_exercises = day_plan.get("exercises", [])
        if not planned_exercises:
            continue

        has_exercises = True
        
        muscles_tracked_today = set()
        total_session_sets = 0
        seen_isolation = False

        for item in planned_exercises:
            ex_id = item["exercise_id"]
            sets = item["sets"]
            reps = item["reps"]
            total_session_sets += sets

            db_ex = EXERCISES.get(ex_id, {})
            ex_type = db_ex.get("type", "Compound").lower()
            movement_pattern = db_ex.get("movement", "").lower()
            ex_name = db_ex.get("name", "Unknown Exercise")

            # Pillar 6: Sequence Audit
            if ex_type == "isolation":
                seen_isolation = True
            elif ex_type == "compound" and seen_isolation:
                session_warnings.append(
                    f"⚠️  {day} Order: '{ex_name}' (Compound) is scheduled after an isolation exercise.\n"
                    f"     Tip: Heavy multi-joint movements require fresh energy and should be done first."
                )

            # Pillar 7: Custom 6-10 Target Rep Range Logic
            if reps > 0 and (reps < 6 or reps > 10):
                session_warnings.append(
                    f"⚠️  {day} Reps: '{ex_name}' is set to {reps} reps.\n"
                    f"     Tip: Muscle fibers grow best when targeted between a 6-10 rep range near failure.\n"
                    f"          If it takes more than 10 reps to reach failure, consider increasing the weight.\n"
                    f"          If you cannot do 6 clean reps, consider reducing the weight."
                )

            # Pillar 10: Biomechanical Redundancy Check
            if movement_pattern:
                daily_movement_redundancy[day][movement_pattern] = daily_movement_redundancy[day].get(movement_pattern, 0) + 1
                if daily_movement_redundancy[day][movement_pattern] > 2:
                    session_warnings.append(
                        f"⚠️  {day} Redundancy: Multiple exercises use the exact same '{movement_pattern.replace('_', ' ').title()}' pattern.\n"
                        f"     Tip: Avoid stacking identical motion lines (e.g. flat bench press + flat machine press) in one day."
                    )

            # Pillar 5: Pulling / Pressing Ratios
            if "push" in movement_pattern:
                push_pull_balance["push"] += sets
            elif "pull" in movement_pattern:
                push_pull_balance["pull"] += sets

            if "extension" in movement_pattern or "squat" in movement_pattern:
                quad_hip_balance["quad_dominant"] += sets
            elif "hinge" in movement_pattern or "curl" in movement_pattern:
                quad_hip_balance["hip_dominant"] += sets

            # Accumulate fine volume fractions
            distribution = db_ex.get("biometric_distribution", {})
            for head_key, factor in distribution.items():
                if head_key in weekly_subdivision_volume:
                    effective_vol = sets * factor
                    weekly_subdivision_volume[head_key] += effective_vol

                    # Find parent muscle bucket to calculate frequency mapping parameters
                    for group_name, sub_heads in muscle_groups_data.items():
                        if head_key in sub_heads:
                            muscles_tracked_today.add(group_name)

        # Update global muscle frequency arrays
        for group in muscles_tracked_today:
            muscle_frequency[group] = muscle_frequency.get(group, 0) + 1

        # Pillar 9: Volume Cap Realism
        if total_session_sets > MAX_SESSION_DURATION_SETS:
            session_warnings.append(
                f"🚨 {day} Overload: Session features {total_session_sets} total sets.\n"
                f"     Warning: Beyond ~22 hard sets, exhaustion sets in and your execution quality completely collapses."
            )

    if not has_exercises:
        print("\nYour weekly plan is completely empty! Add exercises first to run the analysis.")
        return

    # 2. RENDER THE INTERACTIVE SMART ANALYSER NAVIGATION HUB
    while True:
        print("\n" + "#" * 42)
        print("#         🧠 SMART ROUTINE HUB          #")
        print("#" * 42)
        print("1. 🎯 Target Growth & Subdivision Balance")
        print("2. 📅 Frequency & Recovery Audit")
        print("3. ⚖️ Joint Health & Structural Balance")
        print("4. 🔍 Missing Angle Analysis")
        print("5. 🚨 Routine Structure Flags")
        print("6. ↩️ Exit Analyzer")

        hub_choice = input("\nSelect analysis module: ").strip()

        if hub_choice == "6":
            print("\nReturning to Plan Builder...")
            break

        # ====================================================
        # MODULE 1: TARGET GROWTH & SUBDIVISION SELECTOR
        # ====================================================
        elif hub_choice == "1":
            while True:
                print("\n==========================================")
                print("TARGET GROWTH: SELECT MUSCLE GROUP")
                print("==========================================")
                muscle_keys = list(muscle_groups_data.keys())
                for i, group in enumerate(muscle_keys, start=1):
                    print(f"{i}. {group}")
                print("7. ↩️ Back to Hub")

                sub_choice = input("\nChoose muscle to inspect: ").strip()
                if sub_choice == "7":
                    break

                try:
                    selected_group = muscle_keys[int(sub_choice) - 1]
                    print(f"\n--- {selected_group.upper()} GROWTH REPORT ---")

                    # Check if the muscle group is completely unassigned
                    if muscle_frequency.get(selected_group, 0) == 0:
                        print(ignored_group_advice.get(selected_group, f"🔴 No volume mapped to {selected_group}."))
                        continue

                    # Otherwise, iterate over the fine-grained subdivision metrics
                    for head_key in muscle_groups_data[selected_group]:
                        volume = weekly_subdivision_volume[head_key]
                        clean_name = MUSCLES.get(head_key, head_key.replace("_", " ").title())

                        if volume == 0:
                            status = "🔴 MISSED completely (0 Sets planned)"
                        elif volume < MEV:
                            status = f" 🟡 TOO LOW ({volume:.1f} sets | Maintenance level, won't grow fast)"
                        elif volume > MRV:
                            status = f"💥 OVERTRAINING ZONE ({volume:.1f} sets | Dangerously high volume)"
                        else:
                            status = f"✅ PERFECT GROWTH ZONE ({volume:.1f} sets)"
                        print(f" - {clean_name:<28}: {status}")

                except (ValueError, IndexError):
                    print("\nInvalid selection. Choose a number between 1 and 7.")

        # ====================================================
        # MODULE 2: FREQUENCY & RECOVERY ENGINE (WITH IGNORED HIGHLIGHTS)
        # ====================================================
        elif hub_choice == "2":
            print("\n==========================================")
            print("📅 FREQUENCY & RECOVERY CHECK")
            print("==========================================")

            # Print metrics for active muscle structures
            for group, frequency in muscle_frequency.items():
                if frequency > 0:
                    if frequency == 1:
                        print(
                            f" - {group:<15}: 🟡 Hit 1x per week. Research shows "
                            f"splitting your volume across 2 separate days triggers faster growth."
                        )
                    else:
                        print(
                            f" - {group:<15}: ✅ Hit {frequency}x per week. "
                            f"Optimal protein synthesis timing."
                        )

            # Identify and clearly point out completely ignored tracking categories
            print("\n--- 🚫 Missed Training Categories ---")
            ignored_found = False
            for group in muscle_groups_data:
                if muscle_frequency.get(group, 0) == 0:
                    print(
                        f" - {group:<15}: 🔴 IGNORED (0 times in the week. "
                        f"Your body parts will fall out of proportion!)"
                    )
                    ignored_found = True
            if not ignored_found:
                print(" ✅ Great job! Every major muscle category is scheduled at least once this week.")

        # ====================================================
        # MODULE 3: DETAILED JOINT HEALTH STRUCTURAL BALANCE CARD
        # ====================================================
        elif hub_choice == "3":
            print("\n==========================================")
            print("⚖️ JOINT HEALTH & MOVEMENT RATIOS")
            print("==========================================")
            push = push_pull_balance["push"]
            pull = push_pull_balance["pull"]
            quads = quad_hip_balance["quad_dominant"]
            hips = quad_hip_balance["hip_dominant"]

            print(f" 🔲 Upper Body : Pushing Volume = {push:.1f} sets | Pulling Volume = {pull:.1f} sets")
            print(f" 🔲 Lower Body : Quad Focus = {quads:.1f} sets | Hamstring Focus = {hips:.1f} sets")
            print("-" * 42)
            print(" 🧭 HOW TO USE THIS DATA TO GROW AND PREVENT INJURIES:")

            # Upper body structural coaching rule cards
            if push > (pull * 1.5) and pull > 0:
                print("\n🚨 UPPER BODY IMBALANCE DETECTED:")
                print("  Your plan heavily over-indexes on pressing movements (Bench, Shoulder Press).")
                print("  Why this matters: This pulls your shoulders forward, compressing your joints and causing shoulder tears.")
                print("  👉 ACTION PLAN: Add more Pulling work (Rows, Lat Pulldowns) until your Pull volume matches your Push volume.")
            elif push == 0 and pull == 0:
                print("\n Upper Body: No active upper body data calculated yet.")
            else:
                print(
                    "\n✅ UPPER BODY ALIGNMENT: Your push-to-pull layout is highly balanced. "
                    "This preserves smooth rotational mobility and opens up space for maximum muscle growth."
                )

            # Lower body structural coaching rule cards
            if quads > (hips * 2.0) and hips > 0:
                print("\n🚨 LOWER BODY IMBALANCE DETECTED:")
                print("  Your plan is highly knee-dominant, loading quads while ignoring your hamstrings/glutes.")
                print("  Why this matters: This causes knee friction, patellar tendonitis, and limits your overall leg mass potential.")
                print("  👉 ACTION PLAN: Add Romanian Deadlifts, Leg Curls, or Hip Thrusts to balance out your front-to-back muscle tissue.")
            elif quads == 0 and hips == 0:
                print("\n Lower Body: No active lower body data calculated yet.")
            else:
                print(
                    "\n✅ LOWER BODY ALIGNMENT: Your quad-to-hip load setup looks solid. "
                    "This balances knee flexion with hip drive, protecting your joints while building thicker legs."
                )

        # ====================================================
        # MODULE 4: MISSING ANGLE SCANNER (UNCHANGED BY REQUEST)
        # ====================================================
        elif hub_choice == "4":
            print("\n==========================================")
            print("🔍 MISSING ANGLE ANALYSIS")
            print("==========================================")
            missing_gaps = False

            if (weekly_subdivision_volume.get("upper_chest", 0) < 1.0
                    and weekly_subdivision_volume.get("middle_chest", 0) >= 2.0):
                print(" 🔍 Chest: Missing Upper Chest focus. Try replacing a flat bench with Incline Dumbbell Presses.")
                missing_gaps = True

            if (weekly_subdivision_volume.get("lat_width", 0) > 0
                    and weekly_subdivision_volume.get("upper_back", 0) == 0):
                print(" 🔍 Back: Routine lacks horizontal rows. Add Rows to build middle back density.")
                missing_gaps = True

            if (weekly_subdivision_volume.get("triceps_long", 0) < 1.0
                    and weekly_subdivision_volume.get("triceps_outer", 0) >= 2.0):
                print(" 🔍 Triceps: Skipping overhead extension work. Add an overhead tricep stretch movement.")
                missing_gaps = True

            if not missing_gaps:
                print(" ✅ Angle Variation: Superb layout! All target angles are covered perfectly.")

        # ====================================================
        # MODULE 5: ROUTINE FLAGS & RECODE ADJUSTMENT INSTRUCTIONS
        # ====================================================
        elif hub_choice == "5":
            print("\n==========================================")
            print("🚨 ROUTINE STRUCTURE FLAGS")
            print("==========================================")
            if session_warnings:
                for warning in session_warnings:
                    print(warning)
            else:
                print(" ✅ Structure Look Perfect: Your exercise selections and sequencing pass all core efficiency tests.")

            # Render multi-week periodization card check at the bottom
            print("\n--- ⏳ Periodization Strategy ---")
            period_check = input(
                " Is this routine plan meant to be run continuously for more than 6 weeks? (yes/no): "
            ).lower().strip()
            if period_check == "yes":
                print("\n 💡 Coach Tip: To avoid hitting plateaus, make sure to plan a 'Deload Week'")
                print("   every 6-8 weeks where you reduce total planned sets by half for recovery.")

        else:
            print("\nInvalid choice. Select an option from 1 to 6.")

        input("\nPress Enter to return to Analysis Hub Menu...")

# FITNESS APP
# PART 5 — EDIT & MANAGE WORKOUT PLAN
# ============================================================


# ============================================================
# 1. EDIT EXERCISE DETAILS
# ============================================================

def edit_exercise(day):

    exercises = WORKOUT_PLAN[day]["exercises"]

    if not exercises:

        print("\nNo exercises available to edit.")

        return


    print("\n==========================================")
    print(f"EDIT EXERCISE — {day}")
    print("==========================================")


    for number, exercise in enumerate(
        exercises,
        start=1
    ):

        print(
            f"{number}. {exercise['exercise_name']} "
            f"({exercise['sets']} sets × "
            f"{exercise['reps']} reps @ "
            f"{exercise['weight']})"
        )


    while True:

        try:

            choice = int(
                input(
                    "\nSelect exercise number: "
                )
            )


            if 1 <= choice <= len(exercises):

                selected = exercises[choice - 1]

                break


            print(
                "Please select a valid exercise number."
            )


        except ValueError:

            print(
                "Please enter a number."
            )


    print("\nWhat do you want to change?")

    print("1. Sets")
    print("2. Reps")
    print("3. Weight")
    print("4. All")


    while True:

        option = input(
            "\nChoose option: "
        ).strip()


        if option in ["1", "2", "3", "4"]:

            break


        print(
            "Please choose 1, 2, 3, or 4."
        )


    # --------------------------------------------------------
    # CHANGE SETS
    # --------------------------------------------------------

    if option in ["1", "4"]:

        while True:

            try:

                new_sets = int(
                    input("New number of sets: ")
                )

                if new_sets > 0:

                    selected["sets"] = new_sets

                    break

                print(
                    "Sets must be greater than 0."
                )

            except ValueError:

                print(
                    "Please enter a whole number."
                )


    # --------------------------------------------------------
    # CHANGE REPS
    # --------------------------------------------------------

    if option in ["2", "4"]:

        while True:

            try:

                new_reps = int(
                    input("New target reps: ")
                )

                if new_reps >= 0:

                    selected["reps"] = new_reps

                    break

                print(
                    "Reps cannot be negative."
                )

            except ValueError:

                print(
                    "Please enter a whole number."
                )


    # --------------------------------------------------------
    # CHANGE WEIGHT
    # --------------------------------------------------------

    if option in ["3", "4"]:

        while True:

            try:

                new_weight = float(
                    input("New planned weight: ")
                )

                if new_weight >= 0:

                    selected["weight"] = new_weight

                    break

                print(
                    "Weight cannot be negative."
                )

            except ValueError:

                print(
                    "Please enter a valid number."
                )


    print("\nExercise updated successfully.")

    show_day_plan(day)


# ============================================================
# 2. REMOVE EXERCISE
# ============================================================

def remove_exercise(day):

    exercises = WORKOUT_PLAN[day]["exercises"]

    if not exercises:

        print("\nNo exercises available to remove.")

        return


    print("\n==========================================")
    print(f"REMOVE EXERCISE — {day}")
    print("==========================================")


    for number, exercise in enumerate(
        exercises,
        start=1
    ):

        print(
            f"{number}. {exercise['exercise_name']}"
        )


    while True:

        try:

            choice = int(
                input(
                    "\nSelect exercise number to remove: "
                )
            )


            if 1 <= choice <= len(exercises):

                break


            print(
                "Please select a valid exercise number."
            )


        except ValueError:

            print(
                "Please enter a number."
            )


    removed = exercises.pop(choice - 1)


    print(
        f"\n{removed['exercise_name']} "
        "removed successfully."
    )


# ============================================================
# 3. CHANGE BODY PARTS
# ============================================================
def edit_body_parts(day):

    while True:

        print("\n==========================================")
        print(f"BODY PARTS — {day}")
        print("==========================================")

        current_parts = WORKOUT_PLAN[day]["body_parts"]


        print("\nCurrent body parts:")

        if current_parts:

            for number, part in enumerate(
                current_parts,
                start=1
            ):
                print(f"{number}. {part}")

        else:

            print("None")


        print("\nOptions:")

        print("1. Add body part")
        print("2. Remove body part")
        print("3. Replace body parts")
        print("4. Back")


        choice = input(
            "\nChoose option: "
        ).strip()


        # ====================================================
        # ADD BODY PART
        # ====================================================

        if choice == "1":

            available_parts = [
                part
                for part in BODY_PARTS
                if part not in current_parts
            ]


            if not available_parts:

                print(
                    "\nAll available body parts "
                    "are already selected."
                )

                continue


            print("\nAvailable body parts:")

            for number, part in enumerate(
                available_parts,
                start=1
            ):
                print(
                    f"{number}. {part}"
                )


            selection = input(
                "\nEnter numbers to add "
                "(example: 1,3): "
            ).strip()


            try:

                numbers = [
                    int(x.strip())
                    for x in selection.split(",")
                ]


                added = []


                for number in numbers:

                    if (
                        1 <= number
                        <= len(available_parts)
                    ):

                        part = available_parts[
                            number - 1
                        ]

                        if part not in current_parts:

                            current_parts.append(part)

                            added.append(part)


                if added:

                    print(
                        "\nAdded:",
                        ", ".join(added)
                    )

                else:

                    print(
                        "\nNo valid body parts selected."
                    )


            except ValueError:

                print(
                    "\nPlease enter valid numbers."
                )


        # ====================================================
        # REMOVE BODY PART
        # ====================================================

        elif choice == "2":

            if not current_parts:

                print(
                    "\nThere are no body parts to remove."
                )

                continue


            print("\nCurrent body parts:")

            for number, part in enumerate(
                current_parts,
                start=1
            ):
                print(
                    f"{number}. {part}"
                )


            selection = input(
                "\nEnter numbers to remove "
                "(example: 1,3): "
            ).strip()


            try:

                numbers = [
                    int(x.strip())
                    for x in selection.split(",")
                ]


                removed = []


                for number in sorted(
                    numbers,
                    reverse=True
                ):

                    if (
                        1 <= number
                        <= len(current_parts)
                    ):

                        part = current_parts.pop(
                            number - 1
                        )

                        removed.append(part)


                if removed:

                    print(
                        "\nRemoved:",
                        ", ".join(removed)
                    )

                else:

                    print(
                        "\nNo valid body parts selected."
                    )


            except ValueError:

                print(
                    "\nPlease enter valid numbers."
                )


        # ====================================================
        # REPLACE BODY PARTS
        # ====================================================

        elif choice == "3":

            new_body_parts = select_body_parts()


            WORKOUT_PLAN[day][
                "body_parts"
            ] = new_body_parts


            print(
                "\nBody parts replaced successfully."
            )


        # ====================================================
        # BACK
        # ====================================================

        elif choice == "4":

            break


        else:

            print(
                "\nInvalid option."
            )



# ============================================================
# 4. ADD ANOTHER EXERCISE
# ============================================================

def add_another_exercise(day):

    print("\n==========================================")
    print(f"ADD EXERCISE — {day}")
    print("==========================================")


    add_exercise_to_day(day)


# ============================================================
# UPDATED DAY MANAGEMENT
# ============================================================


def manage_day(day):
    while True:
        print("\n==========================================")
        print(f"MANAGE {day.upper()}")
        print("==========================================")

        show_day_plan(day)

        print("\nOptions:")
        print("1. Add exercise")
        print("2. Edit exercise")
        print("3. Remove exercise")
        print("4. Change body parts")
        print("5. Save changes")
        print("6. Finish")

        choice = input("\nChoose option: ").strip()

        if choice == "1":
            add_another_exercise(day)

        elif choice == "2":
            edit_exercise(day)

        elif choice == "3":
            remove_exercise(day)

        elif choice == "4":
            edit_body_parts(day)

        elif choice == "5":
            save_day_plan(day)

        elif choice == "6":
            save_day_plan(day)
            break

        else:
            print("\nInvalid option.")



# ============================================================
# 6. EDIT ANY DAY OF THE WEEK
# ============================================================

def edit_weekly_plan():

    print("\n==========================================")
    print("EDIT WEEKLY PLAN")
    print("==========================================")


    while True:

        day = select_day()


        manage_day(day)


        another = input(
            "\nEdit another day? (yes/no): "
        ).lower().strip()


        if another != "yes":

            break
            
# ============================================================
# FITNESS APP
# PART 6 — WORKOUT LOGGER & WORKOUT HISTORY
# ============================================================


# ============================================================
# 1. ACTUAL WORKOUT HISTORY
# ============================================================

WORKOUT_HISTORY = []


# ============================================================
# 2. CREATE A NEW WORKOUT SESSION
# ============================================================

def create_workout_session(day, workout_type):

    session = {

        "day": day,

        "workout_type": workout_type,

        "date": None,

        "exercises": []

    }

    return session


# ============================================================
# 3. LOG ONE EXERCISE
# ============================================================

def log_exercise(session, exercise_id, planned_data=None):

    exercise = EXERCISES[exercise_id]


    exercise_log = {

        "exercise_id": exercise_id,

        "exercise_name": exercise["name"],

        "planned": planned_data,

        "sets": []

    }


    print("\n==========================================")
    print(
        f"LOGGING: {exercise['name']}"
    )
    print("==========================================")


    # --------------------------------------------------------
    # NUMBER OF SETS
    # --------------------------------------------------------

    while True:

        try:

            number_of_sets = int(
                input(
                    "\nHow many sets did you perform? "
                )
            )

            if number_of_sets > 0:

                break

            print(
                "Number of sets must be greater than 0."
            )

        except ValueError:

            print(
                "Please enter a whole number."
            )


    # --------------------------------------------------------
    # LOG EACH INDIVIDUAL SET
    # --------------------------------------------------------

    for set_number in range(
        1,
        number_of_sets + 1
    ):

        print(
            f"\n--- Set {set_number} ---"
        )


        while True:

            try:

                reps = int(
                    input(
                        "Reps: "
                    )
                )

                if reps >= 0:

                    break

                print(
                    "Reps cannot be negative."
                )

            except ValueError:

                print(
                    "Please enter a whole number."
                )


        while True:

            try:

                weight = float(
                    input(
                        "Weight: "
                    )
                )

                if weight >= 0:

                    break

                print(
                    "Weight cannot be negative."
                )

            except ValueError:

                print(
                    "Please enter a valid number."
                )


        set_data = {

            "set_number": set_number,

            "reps": reps,

            "weight": weight

        }


        exercise_log["sets"].append(
            set_data
        )


    session["exercises"].append(
        exercise_log
    )


    print("\nExercise logged successfully.")


# ============================================================
# 4. LOG AN EXERCISE FROM THE WEEKLY PLAN
# ============================================================

def log_planned_exercise(session, planned_exercise):

    exercise_id = planned_exercise["exercise_id"]


    log_exercise(

        session,

        exercise_id,

        planned_data={

            "sets": planned_exercise["sets"],

            "reps": planned_exercise["reps"],

            "weight": planned_exercise["weight"]

        }

    )


# ============================================================
# 5. START PLANNED ROUTINE
# ============================================================

def start_planned_routine(day):

    planned_exercises = (
        WORKOUT_PLAN[day]["exercises"]
    )


    if not planned_exercises:

        print("\n------------------------------------------")

        print(
            f"You don't have a workout plan for {day}."
        )

        print("------------------------------------------")

        return


    print("\n")
    print("##########################################")
    print(f"# START {day.upper()} ROUTINE")
    print("##########################################")


    session = create_workout_session(

        day,

        "planned"

    )


    print("\nToday's planned exercises:")


    for number, exercise in enumerate(

        planned_exercises,

        start=1

    ):

        print(

            f"{number}. "
            f"{exercise['exercise_name']} — "
            f"{exercise['sets']} × "
            f"{exercise['reps']} @ "
            f"{exercise['weight']}"

        )


    print("\nStarting workout...")


    # --------------------------------------------------------
    # LOG PLANNED EXERCISES
    # --------------------------------------------------------

    for planned_exercise in planned_exercises:

        print("\n")

        print(
            "=========================================="
        )

        print(
            f"NEXT EXERCISE: "
            f"{planned_exercise['exercise_name']}"
        )

        print(
            "=========================================="
        )


        log_planned_exercise(

            session,

            planned_exercise

        )


        # ----------------------------------------------------
        # USER CAN ADD AN EXTRA EXERCISE
        # ----------------------------------------------------

        while True:

            add_extra = input(

                "\nAdd another exercise? (yes/no): "

            ).lower().strip()


            if add_extra == "yes":

                selected_id = select_exercise()


                if selected_id is not None:

                    log_exercise(

                        session,

                        selected_id

                    )

                break


            elif add_extra == "no":

                break

            else:

                print(
                    "Please enter yes or no."
                )


    # --------------------------------------------------------
    # SAVE SESSION
    # --------------------------------------------------------

    finish_workout(session)


# ============================================================
# 6. START FREESTYLE WORKOUT
# ============================================================

def start_freestyle_workout(day):

    print("\n")
    print("##########################################")
    print("#       ADD EXERCISES DIRECTLY           #")
    print("##########################################")


    session = create_workout_session(

        day,

        "freestyle"

    )


    while True:

        print("\n------------------------------------------")

        print(
            "Search for an exercise to add."
        )

        print("------------------------------------------")


        selected_id = select_exercise()


        if selected_id is not None:

            log_exercise(

                session,

                selected_id

            )


        another = input(

            "\nAdd another exercise? (yes/no): "

        ).lower().strip()


        if another != "yes":

            break


    # --------------------------------------------------------
    # SAVE SESSION
    # --------------------------------------------------------

    if session["exercises"]:

        finish_workout(session)

    else:

        print(
            "\nNo exercises were logged."
        )


# ============================================================
# 7. FINISH WORKOUT
# ============================================================

def finish_workout(session):

    print("\n")
    print("##########################################")
    print("#          WORKOUT COMPLETED             #")
    print("##########################################")


    save_workout_session(session)


    print(
        "\nWorkout saved successfully."
    )


    print(
        f"Exercises completed: "
        f"{len(session['exercises'])}"
    )


    print(
        f"Workout type: "
        f"{session['workout_type']}"
    )


# ============================================================
# 8. SHOW TODAY'S WORKOUT SUMMARY
# ============================================================

def show_workout_summary(session):

    print("\n")
    print("==========================================")
    print("WORKOUT SUMMARY")
    print("==========================================")


    print(
        f"Day: {session['day']}"
    )

    print(
        f"Type: {session['workout_type']}"
    )


    for exercise in session["exercises"]:

        print("\n------------------------------------------")

        print(
            exercise["exercise_name"]
        )


        for set_data in exercise["sets"]:

            print(

                f"Set {set_data['set_number']}: "
                f"{set_data['reps']} reps × "
                f"{set_data['weight']}"

            )


    print("\n==========================================")


# ============================================================
# 9. WORKOUT HISTORY
# ============================================================

def show_workout_history():

    print("\n")
    print("##########################################")
    print("#          WORKOUT HISTORY               #")
    print("##########################################")


    if not WORKOUT_HISTORY:

        print(
            "\nNo workouts have been recorded yet."
        )

        return


    for workout_number, session in enumerate(

        WORKOUT_HISTORY,

        start=1

    ):

        print("\n------------------------------------------")

        print(
            f"Workout {workout_number}"
        )

        print(
            f"Day: {session['day']}"
        )

        print(
            f"Type: {session['workout_type']}"
        )


        for exercise in session["exercises"]:

            print(
                f"\n  {exercise['exercise_name']}"
            )


            for set_data in exercise["sets"]:

                print(

                    f"    Set "
                    f"{set_data['set_number']}: "
                    f"{set_data['reps']} reps × "
                    f"{set_data['weight']}"

                )


# ============================================================
# 10. WORKOUT LOGGER MENU
# ============================================================

def workout_logger():

    print("\n")
    print("##########################################")
    print("#          WORKOUT LOGGER                #")
    print("##########################################")


    day = select_day()


    print("\n==========================================")

    print(
        f"WHAT DO YOU WANT TO DO TODAY? — {day}"
    )

    print("==========================================")


    print("1. Start routine")
    print("2. Add exercises directly")
    print("3. View workout history")


    while True:

        choice = input(
            "\nChoose option: "
        ).strip()


        if choice == "1":

            start_planned_routine(day)

            break


        elif choice == "2":

            start_freestyle_workout(day)

            break


        elif choice == "3":

            show_workout_history()

            break


        else:

            print(
                "Please choose 1, 2, or 3."
            )
# ============================================================
# FITNESS APP
# PART 7A — DATABASE SETUP
# ============================================================

import sqlite3


# ============================================================
# 1. DATABASE FILE
# ============================================================

DATABASE_NAME = "fitness_app.db"


# ============================================================
# 2. CONNECT TO DATABASE
# ============================================================

def get_database_connection():

    connection = sqlite3.connect(
        DATABASE_NAME
    )

    connection.row_factory = sqlite3.Row

    return connection
#-------------------------
# ============================================================
# PART 11A — WORKOUT SESSION DATABASE
# ============================================================

def create_workout_history_tables():

    conn = sqlite3.connect("fitness_app.db")

    cursor = conn.cursor()


    # --------------------------------------------------------
    # WORKOUT SESSIONS
    # --------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workout_sessions (

            session_id INTEGER PRIMARY KEY AUTOINCREMENT,

            workout_date TEXT NOT NULL,

            workout_time TEXT NOT NULL,

            day_name TEXT NOT NULL,

            workout_type TEXT NOT NULL,

            created_at TEXT NOT NULL

        )
    """)


    # --------------------------------------------------------
    # EXERCISES PERFORMED IN A SESSION
    # --------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workout_session_exercises (

            session_exercise_id
                INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id INTEGER NOT NULL,

            exercise_id INTEGER NOT NULL,

            exercise_name TEXT NOT NULL,

            exercise_order INTEGER NOT NULL,

            FOREIGN KEY (session_id)
                REFERENCES workout_sessions(session_id)

        )
    """)


    # --------------------------------------------------------
    # INDIVIDUAL SETS
    # --------------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS workout_sets (

            set_id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_exercise_id INTEGER NOT NULL,

            set_number INTEGER NOT NULL,

            reps INTEGER NOT NULL,

            weight REAL NOT NULL,

            FOREIGN KEY (session_exercise_id)
                REFERENCES workout_session_exercises(
                    session_exercise_id
                )

        )
    """)


    conn.commit()

    conn.close()
# ============================================================
# PART 11B — BODY WEIGHT HISTORY
# ============================================================

def create_body_weight_table():

    conn = sqlite3.connect("fitness_app.db")

    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS body_weight_history (

            weight_id INTEGER PRIMARY KEY AUTOINCREMENT,

            weight REAL NOT NULL,

            recorded_date TEXT NOT NULL,

            recorded_time TEXT NOT NULL,

            created_at TEXT NOT NULL

        )
    """)


    conn.commit()

    conn.close()

# ============================================================
# PART 11C — SAVE BODY WEIGHT
# ============================================================

def save_body_weight(weight):

    now = datetime.now()


    recorded_date = now.strftime(
        "%Y-%m-%d"
    )

    recorded_time = now.strftime(
        "%H:%M:%S"
    )

    created_at = now.isoformat()


    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    cursor.execute("""
        INSERT INTO body_weight_history (

            weight,
            recorded_date,
            recorded_time,
            created_at

        )

        VALUES (?, ?, ?, ?)

    """, (

        weight,
        recorded_date,
        recorded_time,
        created_at

    ))


    conn.commit()

    conn.close()


    print(
        f"\nBody weight {weight} kg saved."
    )


# ============================================================
# 3. CREATE DATABASE TABLES
# ============================================================

def initialize_database():

    connection = get_database_connection()

    cursor = connection.cursor()


    # --------------------------------------------------------
    # USER PROFILE
    # --------------------------------------------------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS user_profile (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            age INTEGER,

            height REAL,

            body_weight REAL,

            goal TEXT

        )

    """)


    # --------------------------------------------------------
    # WORKOUT PLANS
    # --------------------------------------------------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS workout_plans (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            day TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

    """)


    # --------------------------------------------------------
    # PLANNED EXERCISES
    # --------------------------------------------------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS planned_exercises (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            plan_id INTEGER NOT NULL,

            exercise_id TEXT NOT NULL,

            exercise_name TEXT NOT NULL,

            sets INTEGER NOT NULL,

            reps INTEGER NOT NULL,

            weight REAL NOT NULL,

            FOREIGN KEY (plan_id)

                REFERENCES workout_plans(id)

        )

    """)


    # --------------------------------------------------------
    # WORKOUT SESSIONS
    # --------------------------------------------------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS workout_sessions (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            day TEXT NOT NULL,

            workout_type TEXT NOT NULL,

            workout_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )

    """)


    # --------------------------------------------------------
    # PERFORMED EXERCISES
    # --------------------------------------------------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS performed_exercises (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            session_id INTEGER NOT NULL,

            exercise_id TEXT NOT NULL,

            exercise_name TEXT NOT NULL,

            FOREIGN KEY (session_id)

                REFERENCES workout_sessions(id)

        )

    """)


    # --------------------------------------------------------
    # INDIVIDUAL SETS
    # --------------------------------------------------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS performed_sets (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            performed_exercise_id INTEGER NOT NULL,

            set_number INTEGER NOT NULL,

            reps INTEGER NOT NULL,

            weight REAL NOT NULL,

            FOREIGN KEY (performed_exercise_id)

                REFERENCES performed_exercises(id)

        )

    """)


    connection.commit()

    connection.close()
# ============================================================
# PART 7B — USER PROFILE STORAGE
# ============================================================


def save_user_profile(
    age,
    height,
    body_weight,
    goal
):

    connection = get_database_connection()

    cursor = connection.cursor()


    cursor.execute("""

        INSERT INTO user_profile (

            age,
            height,
            body_weight,
            goal

        )

        VALUES (?, ?, ?, ?)

    """, (

        age,
        height,
        body_weight,
        goal

    ))


    connection.commit()

    connection.close()


# ============================================================
# LOAD USER PROFILE
# ============================================================

def load_user_profile():

    connection = get_database_connection()

    cursor = connection.cursor()


    cursor.execute("""

        SELECT *

        FROM user_profile

        ORDER BY id DESC

        LIMIT 1

    """)


    profile = cursor.fetchone()


    connection.close()


    if profile is None:

        return None


    return dict(profile)
# ============================================================
# PART 7C — WORKOUT SESSION STORAGE
# ============================================================


def save_workout_session(session):

    connection = get_database_connection()

    cursor = connection.cursor()


    # --------------------------------------------------------
    # CREATE WORKOUT SESSION
    # --------------------------------------------------------

    cursor.execute("""

        INSERT INTO workout_sessions (

            day,
            workout_type

        )

        VALUES (?, ?)

    """, (

        session["day"],

        session["workout_type"]

    ))


    session_id = cursor.lastrowid


    # --------------------------------------------------------
    # SAVE EVERY EXERCISE
    # --------------------------------------------------------

    for exercise in session["exercises"]:


        cursor.execute("""

            INSERT INTO performed_exercises (

                session_id,
                exercise_id,
                exercise_name

            )

            VALUES (?, ?, ?)

        """, (

            session_id,

            exercise["exercise_id"],

            exercise["exercise_name"]

        ))


        performed_exercise_id = cursor.lastrowid


        # ----------------------------------------------------
        # SAVE EVERY INDIVIDUAL SET
        # ----------------------------------------------------

        for set_data in exercise["sets"]:

            cursor.execute("""

                INSERT INTO performed_sets (

                    performed_exercise_id,
                    set_number,
                    reps,
                    weight

                )

                VALUES (?, ?, ?, ?)

            """, (

                performed_exercise_id,

                set_data["set_number"],

                set_data["reps"],

                set_data["weight"]

            ))


    connection.commit()

    connection.close()
# ============================================================
# PART 7D — LOAD WORKOUT HISTORY
# ============================================================


def load_workout_history():

    connection = get_database_connection()

    cursor = connection.cursor()


    cursor.execute("""

        SELECT *

        FROM workout_sessions

        ORDER BY workout_date ASC

    """)


    sessions = cursor.fetchall()


    workout_history = []


    for session_row in sessions:


        session = {

            "id": session_row["id"],

            "day": session_row["day"],

            "workout_type": session_row["workout_type"],

            "date": session_row["workout_date"],

            "exercises": []

        }


        cursor.execute("""

            SELECT *

            FROM performed_exercises

            WHERE session_id = ?

            ORDER BY id

        """, (

            session_row["id"],

        ))


        exercises = cursor.fetchall()


        for exercise_row in exercises:


            exercise = {

                "exercise_id":
                    exercise_row["exercise_id"],

                "exercise_name":
                    exercise_row["exercise_name"],

                "sets": []

            }


            cursor.execute("""

                SELECT *

                FROM performed_sets

                WHERE performed_exercise_id = ?

                ORDER BY set_number

            """, (

                exercise_row["id"],

            ))


            sets = cursor.fetchall()


            for set_row in sets:

                exercise["sets"].append({

                    "set_number":
                        set_row["set_number"],

                    "reps":
                        set_row["reps"],

                    "weight":
                        set_row["weight"]

                })


            session["exercises"].append(
                exercise
            )


        workout_history.append(
            session
        )


    connection.close()


    return workout_history
# ============================================================
# DATABASE INITIALIZATION
# ============================================================

initialize_database()
# ============================================================
# FITNESS APP
# PART 8A — BODY PART STORAGE
# ============================================================


def initialize_plan_database():

    connection = get_database_connection()

    cursor = connection.cursor()


    # --------------------------------------------------------
    # BODY PARTS FOR EACH WORKOUT PLAN
    # --------------------------------------------------------

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS plan_body_parts (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            plan_id INTEGER NOT NULL,

            body_part TEXT NOT NULL,

            FOREIGN KEY (plan_id)

                REFERENCES workout_plans(id)

        )

    """)


    connection.commit()

    connection.close()
# ============================================================
# PART 8B — SAVE ONE DAY'S PLAN
# ============================================================


def save_day_plan(day):

    connection = get_database_connection()

    cursor = connection.cursor()


    # --------------------------------------------------------
    # REMOVE OLD PLAN FOR THIS DAY
    # --------------------------------------------------------

    cursor.execute("""

        SELECT id

        FROM workout_plans

        WHERE day = ?

    """, (day,))


    old_plan = cursor.fetchone()


    if old_plan:

        old_plan_id = old_plan["id"]


        cursor.execute("""

            DELETE FROM plan_body_parts

            WHERE plan_id = ?

        """, (old_plan_id,))


        cursor.execute("""

            DELETE FROM planned_exercises

            WHERE plan_id = ?

        """, (old_plan_id,))


        cursor.execute("""

            DELETE FROM workout_plans

            WHERE id = ?

        """, (old_plan_id,))


    # --------------------------------------------------------
    # CREATE NEW PLAN
    # --------------------------------------------------------

    cursor.execute("""

        INSERT INTO workout_plans (day)

        VALUES (?)

    """, (day,))


    plan_id = cursor.lastrowid


    # --------------------------------------------------------
    # SAVE BODY PARTS
    # --------------------------------------------------------

    for body_part in WORKOUT_PLAN[day]["body_parts"]:

        cursor.execute("""

            INSERT INTO plan_body_parts (

                plan_id,
                body_part

            )

            VALUES (?, ?)

        """, (

            plan_id,
            body_part

        ))


    # --------------------------------------------------------
    # SAVE PLANNED EXERCISES
    # --------------------------------------------------------

    for exercise in WORKOUT_PLAN[day]["exercises"]:

        cursor.execute("""

            INSERT INTO planned_exercises (

                plan_id,
                exercise_id,
                exercise_name,
                sets,
                reps,
                weight

            )

            VALUES (?, ?, ?, ?, ?, ?)

        """, (

            plan_id,

            exercise["exercise_id"],

            exercise["exercise_name"],

            exercise["sets"],

            exercise["reps"],

            exercise["weight"]

        ))


    connection.commit()

    connection.close()


    print(
        f"\n{day} plan saved successfully."
    )
# ============================================================
# PART 8C — LOAD WEEKLY PLAN FROM DATABASE
# ============================================================


def load_workout_plan():

    connection = get_database_connection()

    cursor = connection.cursor()


    # --------------------------------------------------------
    # CLEAR CURRENT MEMORY PLAN
    # --------------------------------------------------------

    for day in DAYS:

        WORKOUT_PLAN[day]["body_parts"] = []

        WORKOUT_PLAN[day]["exercises"] = []


    # --------------------------------------------------------
    # LOAD EACH DAY
    # --------------------------------------------------------

    cursor.execute("""

        SELECT *

        FROM workout_plans

        ORDER BY id

    """)


    plans = cursor.fetchall()


    for plan in plans:

        day = plan["day"]

        plan_id = plan["id"]


        # ----------------------------------------------------
        # LOAD BODY PARTS
        # ----------------------------------------------------

        cursor.execute("""

            SELECT body_part

            FROM plan_body_parts

            WHERE plan_id = ?

            ORDER BY id

        """, (plan_id,))


        body_parts = cursor.fetchall()


        for body_part in body_parts:

            WORKOUT_PLAN[day]["body_parts"].append(

                body_part["body_part"]

            )


        # ----------------------------------------------------
        # LOAD EXERCISES
        # ----------------------------------------------------

        cursor.execute("""

            SELECT *

            FROM planned_exercises

            WHERE plan_id = ?

            ORDER BY id

        """, (plan_id,))


        exercises = cursor.fetchall()


        for exercise in exercises:

            WORKOUT_PLAN[day]["exercises"].append({

                "exercise_id":
                    exercise["exercise_id"],

                "exercise_name":
                    exercise["exercise_name"],

                "sets":
                    exercise["sets"],

                "reps":
                    exercise["reps"],

                "weight":
                    exercise["weight"]

            })


    connection.close()
# ============================================================
# LOAD SAVED WORKOUT PLAN
# ============================================================

# 1. Create the database files and empty tables first
initialize_database()
initialize_plan_database()

# 2. Load any existing user workout data into the app memory
load_workout_plan()

# 3. Start the actual interactive application loop
#workout_plan_builder()

    
# ============================================================
# PART 9A — GET TODAY'S DAY
# ============================================================

def get_today_day():

    return datetime.now().strftime("%A")

# ============================================================
# PART 9B — START TODAY'S WORKOUT PLAN
# ============================================================
def create_session_from_plan(day):
    """
    Creates an active, copyable layout of the user's weekly routine 
    for tracking current workout sets.
    """
    import copy
    
    plan = WORKOUT_PLAN[day]
    
    session_data = {
        "day": day,
        "workout_type": "planned",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "exercises": []
    }
    
    for exercise in plan.get("exercises", []):
        session_data["exercises"].append(copy.deepcopy(exercise))
        
    return session_data
 #============================================================
# PART 9A — START TODAY'S WORKOUT PLAN
# ============================================================

def start_todays_workout_plan():

    today = get_today_day()

    print("\n")
    print("##########################################")
    print("#       START TODAY'S WORKOUT            #")
    print("##########################################")

    print(f"\nToday: {today}")


    # --------------------------------------------------------
    # CHECK WEEKLY PLAN
    # --------------------------------------------------------

    today_plan = WORKOUT_PLAN.get(today)


    if not today_plan:

        print(
            f"\nNo workout plan found for {today}."
        )

        print(
            "\nReturning to Start Workout menu..."
        )

        return


    if not today_plan["exercises"]:

        print(
            f"\nYou don't have any exercises "
            f"planned for {today}."
        )

        print(
            "\nReturning to Start Workout menu..."
        )

        return


    # --------------------------------------------------------
    # CREATE A SEPARATE TODAY SESSION
    # --------------------------------------------------------

    session = create_session_from_plan(
        today
    )


    print(
        f"\n{today}'s workout plan loaded."
    )


    # --------------------------------------------------------
    # OPEN TODAY'S WORKOUT SCREEN
    # --------------------------------------------------------

    todays_workout_screen(
        session
    )
# ============================================================
# PART 9B — TODAY'S WORKOUT SCREEN
# ============================================================

def todays_workout_screen(session):

    while True:

        print("\n")
        print("##########################################")
        print(
            f"#          {session['day'].upper()} WORKOUT"
        )
        print("##########################################")


        # ----------------------------------------------------
        # SHOW EXERCISES
        # ----------------------------------------------------

        if session["exercises"]:

            print("\nExercises:")

            for number, exercise in enumerate(

                session["exercises"],

                start=1

            ):

                print(
                    f"{number}. "
                    f"{exercise['exercise_name']}"
                )

        else:

            print(
                "\nNo exercises in today's workout."
            )


        # ----------------------------------------------------
        # OPTIONS
        # ----------------------------------------------------

        print("\n")

        print("A. Select Exercise")

        print("B. Add Exercise")

        print("C. Finish Workout")

        print("D. Exit Workout")


        choice = input(
            "\nChoose option: "
        ).strip().lower()


        # ----------------------------------------------------
        # SELECT EXISTING EXERCISE
        # ----------------------------------------------------

        if choice == "a":

            if not session["exercises"]:

                print(
                    "\nNo exercises available."
                )

                continue


            select_and_log_exercise(
                session
            )


        # ----------------------------------------------------
        # ADD NEW EXERCISE
        # ----------------------------------------------------

        elif choice == "b":

            add_exercise_to_session(
                session
            )


        # ----------------------------------------------------
        # FINISH
        # ----------------------------------------------------

        elif choice == "c":

            if not session["exercises"]:

                print(
                    "\nNo exercises have been added."
                )

                continue


            finish_logged_workout(
                session
            )

            break


        # ----------------------------------------------------
        # EXIT WITHOUT SAVING
        # ----------------------------------------------------

        elif choice == "d":

            confirm = input(
                "\nExit workout without saving? "
                "(yes/no): "
            ).lower().strip()


            if confirm == "yes":

                print(
                    "\nWorkout discarded."
                )

                break


        else:

            print(
                "\nInvalid option."
            )
# ============================================================
# PART 9C — SELECT AND LOG EXERCISE
# ============================================================

def select_and_log_exercise(session):

    print("\n")
    print("==========================================")
    print("SELECT EXERCISE")
    print("==========================================")


    for number, exercise in enumerate(

        session["exercises"],

        start=1

    ):

        print(
            f"{number}. "
            f"{exercise['exercise_name']}"
        )


    while True:

        try:

            choice = int(
                input(
                    "\nSelect exercise number: "
                )
            )


            if 1 <= choice <= len(
                session["exercises"]
            ):

                break


            print(
                "\nInvalid exercise number."
            )


        except ValueError:

            print(
                "\nPlease enter a number."
            )


    selected_exercise = session[
        "exercises"
    ][choice - 1]


    log_planned_exercise(session,
        selected_exercise
    )

# ============================================================
# PART 9C — ADD WORKOUT
# ============================================================
# ============================================================
# ADD EXERCISE TO TODAY'S WORKOUT SESSION
# ============================================================

# ============================================================
# ADD EXERCISE TO TODAY'S WORKOUT SESSION
# ============================================================

# ============================================================
# PART 13A — ADD EXERCISE TO WORKOUT SESSION
# SET-BY-SET LOGGING
# ============================================================

# ============================================================
# PART 13D-1 — ADD EXERCISE TO WORKOUT SESSION
# ============================================================

def add_exercise_to_session(session):

    print("\n==========================================")
    print("ADD EXERCISE TO TODAY'S WORKOUT")
    print("==========================================")


    selected_id = select_exercise()


    if selected_id is None:

        return False


    exercise = EXERCISES[selected_id]


    exercise_data = {

        "exercise_id": selected_id,

        "exercise_name": exercise["name"],

        "sets": []

    }


    # --------------------------------------------------------
    # NUMBER OF SETS
    # --------------------------------------------------------

    while True:

        try:

            number_of_sets = int(
                input(
                    "\nHow many sets did you perform? "
                )
            )


            if number_of_sets > 0:

                break


            print(
                "Number of sets must be greater than 0."
            )


        except ValueError:

            print(
                "Please enter a whole number."
            )


    # --------------------------------------------------------
    # LOG EACH SET
    # --------------------------------------------------------

    for set_number in range(
        1,
        number_of_sets + 1
    ):

        print(
            f"\n---------- SET {set_number} ----------"
        )


        while True:

            try:

                reps = int(
                    input(
                        "Reps: "
                    )
                )


                if reps >= 0:

                    break


                print(
                    "Reps cannot be negative."
                )


            except ValueError:

                print(
                    "Please enter a whole number."
                )


        while True:

            try:

                weight = float(
                    input(
                        "Weight (kg): "
                    )
                )


                if weight >= 0:

                    break


                print(
                    "Weight cannot be negative."
                )


            except ValueError:

                print(
                    "Please enter a valid number."
                )


        exercise_data["sets"].append({

            "set_number": set_number,

            "reps": reps,

            "weight": weight

        })


    session["exercises"].append(
        exercise_data
    )


    print("\n==========================================")

    print(
        f"{exercise['name']} added "
        "to today's workout."
    )


    print("\nLogged sets:")


    for workout_set in exercise_data["sets"]:

        print(
            f"Set {workout_set['set_number']}: "
            f"{workout_set['reps']} reps × "
            f"{workout_set['weight']} kg"
        )


    print("==========================================")


    return True
    
# ============================================================
# PART 13D-2 — ADD SET
# ============================================================

def add_set_to_exercise(exercise):

    set_number = len(
        exercise["sets"]
    ) + 1


    print(
        f"\n---------- SET {set_number} ----------"
    )


    # --------------------------------------------------------
    # REPS
    # --------------------------------------------------------

    while True:

        try:

            reps = int(
                input(
                    "Reps: "
                )
            )


            if reps >= 0:

                break


            print(
                "Reps cannot be negative."
            )


        except ValueError:

            print(
                "Please enter a whole number."
            )


    # --------------------------------------------------------
    # WEIGHT
    # --------------------------------------------------------

    while True:

        try:

            weight = float(
                input(
                    "Weight (kg): "
                )
            )


            if weight >= 0:

                break


            print(
                "Weight cannot be negative."
            )


        except ValueError:

            print(
                "Please enter a valid number."
            )


    exercise["sets"].append({

        "set_number": set_number,

        "reps": reps,

        "weight": weight

    })


    print(
        f"\nSet {set_number} added."
    )

# ============================================================
# PART 13D-3 — EDIT SET
# ============================================================

def edit_set(exercise):

    if not exercise["sets"]:

        print(
            "\nNo sets available."
        )

        return


    print(
        f"\n{exercise['exercise_name']}"
    )


    for workout_set in exercise["sets"]:

        print(
            f"{workout_set['set_number']}. "
            f"{workout_set['reps']} reps × "
            f"{workout_set['weight']} kg"
        )


    try:

        choice = int(
            input(
                "\nSelect set to edit: "
            )
        )


        if not (
            1 <= choice
            <= len(exercise["sets"])
        ):

            print(
                "\nInvalid set."
            )

            return


    except ValueError:

        print(
            "\nPlease enter a number."
        )

        return


    selected_set = exercise[
        "sets"
    ][choice - 1]


    # --------------------------------------------------------
    # NEW REPS
    # --------------------------------------------------------

    while True:

        try:

            reps = int(
                input(
                    "New reps: "
                )
            )


            if reps >= 0:

                break


            print(
                "Reps cannot be negative."
            )


        except ValueError:

            print(
                "Please enter a whole number."
            )


    # --------------------------------------------------------
    # NEW WEIGHT
    # --------------------------------------------------------

    while True:

        try:

            weight = float(
                input(
                    "New weight (kg): "
                )
            )


            if weight >= 0:

                break


            print(
                "Weight cannot be negative."
            )


        except ValueError:

            print(
                "Please enter a valid number."
            )


    selected_set["reps"] = reps

    selected_set["weight"] = weight


    print(
        "\nSet updated successfully."
    )

# ============================================================
# PART 13D-4 — REMOVE SET
# ============================================================

def remove_set(exercise):

    if not exercise["sets"]:

        print(
            "\nNo sets available."
        )

        return


    print(
        f"\n{exercise['exercise_name']}"
    )


    for workout_set in exercise["sets"]:

        print(
            f"{workout_set['set_number']}. "
            f"{workout_set['reps']} reps × "
            f"{workout_set['weight']} kg"
        )


    try:

        choice = int(
            input(
                "\nSelect set to remove: "
            )
        )


        if not (
            1 <= choice
            <= len(exercise["sets"])
        ):

            print(
                "\nInvalid set."
            )

            return


    except ValueError:

        print(
            "\nPlease enter a number."
        )

        return


    removed_set = exercise[
        "sets"
    ].pop(choice - 1)


    # --------------------------------------------------------
    # RE-NUMBER REMAINING SETS
    # --------------------------------------------------------

    for number, workout_set in enumerate(

        exercise["sets"],

        start=1

    ):

        workout_set["set_number"] = number


    print(
    "\nSet removed successfully.")

# ============================================================
# PART 13D-5 — EDIT EXERCISE
# ============================================================

def edit_workout_exercise(session):

    if not session["exercises"]:

        print(
            "\nNo exercises available."
        )

        return


    print("\nToday's Exercises:")


    for number, exercise in enumerate(

        session["exercises"],

        start=1

    ):

        print(
            f"{number}. "
            f"{exercise['exercise_name']}"
        )


    try:

        choice = int(
            input(
                "\nSelect exercise: "
            )
        )


        if not (
            1 <= choice
            <= len(session["exercises"])
        ):

            print(
                "\nInvalid exercise."
            )

            return


    except ValueError:

        print(
            "\nPlease enter a number."
        )

        return


    exercise = session[
        "exercises"
    ][choice - 1]


    while True:

        print("\n==========================================")

        print(
            exercise["exercise_name"]
        )

        print("==========================================")


        if exercise["sets"]:

            for workout_set in exercise["sets"]:

                print(
                    f"Set {workout_set['set_number']}: "
                    f"{workout_set['reps']} reps × "
                    f"{workout_set['weight']} kg"
                )

        else:

            print("No sets.")


        print("\nOptions:")

        print("1. Add Set")
        print("2. Edit Set")
        print("3. Remove Set")
        print("4. Back")


        option = input(
            "\nChoose option: "
        ).strip()


        if option == "1":

            add_set_to_exercise(
                exercise
            )


        elif option == "2":

            edit_set(
                exercise
            )


        elif option == "3":

            remove_set(
                exercise
            )


        elif option == "4":

            break


        else:

            print(
                "\nInvalid option."
            )

# ============================================================
# PART 13B — FINISH AND SAVE WORKOUT
# ============================================================

def finish_logged_workout(session):

    connection = get_database_connection()

    cursor = connection.cursor()


    try:

        # ----------------------------------------------------
        # SAVE WORKOUT SESSION
        # ----------------------------------------------------

        cursor.execute("""
            INSERT INTO workout_sessions (
                day,
                workout_type,
                workout_date
            )

            VALUES (?, ?, ?)
        """, (

            session["day"],

            session["workout_type"],

            f"{session['date']} {session['time']}"

        ))


        session_id = cursor.lastrowid


        # ----------------------------------------------------
        # SAVE EACH EXERCISE
        # ----------------------------------------------------

        for exercise in session["exercises"]:

            cursor.execute("""
                INSERT INTO performed_exercises (
                    session_id,
                    exercise_id,
                    exercise_name
                )

                VALUES (?, ?, ?)
            """, (

                session_id,

                exercise["exercise_id"],

                exercise["exercise_name"]

            ))


            performed_exercise_id = (
                cursor.lastrowid
            )


            # ------------------------------------------------
            # SAVE EACH INDIVIDUAL SET
            # ------------------------------------------------

            for workout_set in exercise["sets"]:

                cursor.execute("""
                    INSERT INTO performed_sets (
                        performed_exercise_id,
                        set_number,
                        reps,
                        weight
                    )

                    VALUES (?, ?, ?, ?)
                """, (

                    performed_exercise_id,

                    workout_set["set_number"],

                    workout_set["reps"],

                    workout_set["weight"]

                ))


        # ----------------------------------------------------
        # COMMIT EVERYTHING
        # ----------------------------------------------------

        connection.commit()


        print("\n")
        print("##########################################")
        print("#         WORKOUT SAVED SUCCESSFULLY     #")
        print("##########################################")


        print(
            f"\nDate: {session['date']}"
        )

        print(
            f"Time: {session['time']}"
        )

        print(
            f"Workout type: "
            f"{session['workout_type']}"
        )


        print(
            "\nYour workout has been saved."
        )


    except Exception as error:

        # ----------------------------------------------------
        # ROLLBACK IF ANYTHING GOES WRONG
        # ----------------------------------------------------

        connection.rollback()


        print("\n")
        print("##########################################")
        print("#          WORKOUT SAVE FAILED           #")
        print("##########################################")


        print(
            f"\nError: {error}"
        )


    finally:

        connection.close()

# ============================================================
# PART 9 — ADD WORKOUT WITHOUT WEEKLY PLAN

def remove_exercise_from_session(session):
    """
    Removes an exercise track entirely from the active workout session state.
    """
    if not session["exercises"]:
        print("\nNo exercises inside today's session log to remove.")
        return

    print("\nSelect exercise to remove:")
    for i, ex in enumerate(session["exercises"], start=1):
        print(f"{i}. {ex['exercise_name']}")

    try:
        choice = int(input("\nSelect exercise number: "))
        if 1 <= choice <= len(session["exercises"]):
            removed = session["exercises"].pop(choice - 1)
            print(f"\n{removed['exercise_name']} removed from current session.")
        else:
            print("\nInvalid selection number.")
    except ValueError:
        print("\nPlease type a valid numeric value.")


# ============================================================

def add_workout():
    today = get_today_day()
    session = {
        "day": today,
        "workout_type": "freestyle",
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "exercises": []
    }

    while True:
        print("\n")
        print("##########################################")
        print("#              ADD WORKOUT               #")
        print("##########################################")
        print(f"\nToday: {today}")

        # ----------------------------------------------------
        # SHOW CURRENT EXERCISES
        # ----------------------------------------------------
        if session["exercises"]:
            print("\nToday's Exercises:")
            for number, exercise in enumerate(session["exercises"], start=1):
                print(f"{number}. {exercise['exercise_name']}")
        else:
            print("\nNo exercises added yet.")

        # ----------------------------------------------------
        # OPTIONS
        # ----------------------------------------------------
        print("\n1. Add Exercise")
        print("2. Edit Exercise")
        print("3. Remove Exercise")
        print("4. Finish Workout")
        print("5. Exit")

        choice = input("\nChoose option: ").strip()

        # ----------------------------------------------------
        # MENU SELECTION HANDLING
        # ----------------------------------------------------
        if choice == "1":
            add_exercise_to_session(session)

        elif choice == "2":
            edit_workout_exercise(session)

        elif choice == "3":
            remove_exercise_from_session(session)

        elif choice == "4":
            if not session["exercises"]:
                print(
                    "\nYou must add at least "
                    "one exercise first."
                )
                continue
            finish_logged_workout(session)
            break

        elif choice == "5":
            confirm = input(
                "\nExit without saving? (yes/no): "
            ).lower().strip()
            if confirm == "yes":
                print("\nWorkout cancelled.")
                break



# ============================================================
# PART 9D — WORKOUT LOGGER
# ============================================================

# ============================================================
# PART 13D-6 — EDITABLE WORKOUT LOGGER
# ============================================================

def workout_logger(session):

    while True:

        print("\n")
        print("==========================================")
        print("             WORKOUT LOGGER")
        print("==========================================")


        # ----------------------------------------------------
        # SHOW CURRENT WORKOUT
        # ----------------------------------------------------

        if session["exercises"]:

            show_today_workout(session)
                
            

        else:

            print(
                "\nNo exercises added yet."
            )


        print("\nOptions:")

        print("1. Edit exercise")
        print("2. Add exercise")
        print("3. Remove exercise")
        print("4. Finish workout")
        print("5. Cancel workout")


        choice = input(
            "\nChoose option: "
        ).strip()


        # ----------------------------------------------------
        # EDIT EXERCISE
        # ----------------------------------------------------

        if choice == "1":

            edit_workout_exercise(
                session
            )


        # ----------------------------------------------------
        # ADD EXERCISE
        # ----------------------------------------------------

        elif choice == "2":

            add_exercise_to_session(
                session
            )


        # ----------------------------------------------------
        # REMOVE EXERCISE
        # ----------------------------------------------------

        elif choice == "3":

            remove_exercise_from_session(
                session
            )


        # ----------------------------------------------------
        # FINISH WORKOUT
        # ----------------------------------------------------

        elif choice == "4":

            if not session["exercises"]:

                print(
                    "\nYou haven't added "
                    "any exercises."
                )

                continue


            finish_logged_workout(
                session
            )

            break


        # ----------------------------------------------------
        # CANCEL WORKOUT
        # ----------------------------------------------------

        elif choice == "5":

            confirm = input(
                "\nCancel this workout? "
                "(yes/no): "
            ).lower().strip()


            if confirm == "yes":

                print(
                    "\nWorkout cancelled."
                )

                break


        else:

            print(
                "\nInvalid option."
            )
# ============================================================
# FITNESS APP
# PART 10A — START WORKOUT MENU
# ============================================================


def start_workout_menu():

    while True:

        print("\n")
        print("##########################################")
        print("#             START WORKOUT              #")
        print("##########################################")

        print("\n1. Start Today's Workout Plan")
        print("2. Add Workout")
        print("3. Back")

        choice = input(
            "\nChoose option: "
        ).strip()


        # ----------------------------------------------------
        # TODAY'S PLANNED WORKOUT
        # ----------------------------------------------------

        if choice == "1":

            start_todays_workout_plan()


        # ----------------------------------------------------
        # FREESTYLE WORKOUT
        # ----------------------------------------------------

        elif choice == "2":

            add_workout()


        # ----------------------------------------------------
        # BACK
        # ----------------------------------------------------

        elif choice == "3":

            break


        else:

            print(
                "\nInvalid option. "
                "Please choose 1, 2, or 3."
            )
# ============================================================
# PART 10B — MAIN APPLICATION MENU
# ============================================================
# ==========================================================
# PART 11D - VIEW BODY WEIGHT HISTORY
# ==========================================================

def view_body_weight_history():
    # Make sure to change 'fitness_app.db' if you aren't using DB_NAME
    conn = sqlite3.connect('fitness_app.db')
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT 
            weight,
            recorded_date,
            recorded_time
        FROM body_weight_history
        ORDER BY 
            recorded_date ASC,
            recorded_time ASC
    """)
    
    records = cursor.fetchall()
    conn.close()
    
    print("\n")
    print("##########################################")
    print("#           BODY WEIGHT HISTORY          #")
    print("##########################################")
    
    if not records:
        print("\nNo body weight records found.")
        return
        
    for row in records:
        # Note: If fetchall returns sqlite3.Row or tuples, 
        # using indexing works best:
        weight = row[0]
        date = row[1]
        time = row[2]
        print(f"\n{date} {time}")
        print(f"Weight: {weight} kg")
# ==========================================================
# USER PROFILE INTERFACE AND DASHBOARD
# ==========================================================
def create_profile_interface():
    connection = get_database_connection()
    cursor = connection.cursor()
    
    # FIX: Fetch the absolute LATEST entry in the database table instead of the frozen first row
    cursor.execute("SELECT id, age, height, body_weight, goal FROM user_profile ORDER BY id DESC LIMIT 1")
    profile = cursor.fetchone()
    
    # Establish dynamic defaults from database context states
    current_age = str(profile["age"]) if profile else ""
    current_height = str(profile["height"]) if profile else ""
    current_weight = str(profile["body_weight"]) if profile else ""
    current_goal = str(profile["goal"]).strip() if profile else "Not Set"

    GOAL_OPTIONS = [
        "Hypertrophy (Muscle Mass)",
        "Strength Gain",
        "Fat Loss",
        "Muscular Endurance",
        "Power/Explosiveness (Sport Performance)",
        "General Fitness/Health"
    ]

    def prompt_for_goal(existing_goal):
        print("\nSelect your primary training goal:")
        for idx, goal_name in enumerate(GOAL_OPTIONS, start=1):
            print(f"{idx}. {goal_name}")
        print("0. Keep current goal")
        
        while True:
            choice = input(f"\nChoose goal number (Current: {existing_goal.title()}): ").strip()
            if choice == "0" or choice == "":
                return existing_goal if existing_goal != "Not Set" else "Hypertrophy (Muscle Mass)"
            try:
                choice_num = int(choice)
                if 1 <= choice_num <= 6:
                    return GOAL_OPTIONS[choice_num - 1]
                print("Please enter a valid choice between 1 and 6.")
            except ValueError:
                print("Please enter a number or press Enter to keep current.")

    # Show the User Profile Card Dashboard Screen
    print("\n==========================================")
    print("             USER PROFILE                 ")
    print("==========================================")
    print(f"Age:    {current_age if current_age else 'Not Set'} years")
    print(f"Height: {current_height if current_height else 'Not Set'} cm")
    print(f"Weight: {current_weight if current_weight else 'Not Set'} kg")
    print(f"Goal:   {current_goal.title()}")
    print("==========================================")
    print("Options:")
    print("1. Update Profile Info & Goal")
    print("2. Back to Main Menu")
    
    choice = input("\nChoose option: ").strip()
    
    if choice == "1":
        print("\n--- Update Profile (Press Enter to keep current value) ---")
        
        new_age = input(f"Enter your age [{current_age}]: ").strip()
        age = int(new_age) if new_age != "" else (int(current_age) if current_age else None)
        
        new_height = input(f"Enter your height in cm [{current_height}]: ").strip()
        height = float(new_height) if new_height != "" else (float(current_height) if current_height else None)
        
        new_weight = input(f"Enter your body weight in kg [{current_weight}]: ").strip()
        weight = float(new_weight) if new_weight != "" else (float(current_weight) if current_weight else None)
        
        selected_goal = prompt_for_goal(current_goal)
        
        # FIX: Explicitly perform an UPDATE if editing a row, otherwise insert the first user seed row
        if profile:
            cursor.execute("""
                UPDATE user_profile 
                SET age = ?, height = ?, body_weight = ?, goal = ?
                WHERE id = ?
            """, (age, height, weight, selected_goal, profile["id"]))
            connection.commit()
            print("\n🔄 Profile successfully updated in database memory!")
        else:
            cursor.execute("""
                INSERT INTO user_profile (age, height, body_weight, goal)
                VALUES (?, ?, ?, ?)
            """, (age, height, weight, selected_goal))
            connection.commit()
            print("\n Profile created successfully!")
            
        connection.close()
        return
        
    connection.close()



# ============================================================
# START WORKOUT MENU
# ============================================================

def start_workout_menu():

    while True:

        print("\n")
        print("##########################################")
        print("#              START WORKOUT             #")
        print("##########################################")

        print("\n1. Start today's workout")
        print("2. Add Workout")
        print("3. Exit")


        choice = input(
            "\nChoose option: "
        ).strip()


        # ----------------------------------------------------
        # START TODAY'S PLANNED WORKOUT
        # ----------------------------------------------------

        if choice == "1":

            start_todays_workout_plan()


        # ----------------------------------------------------
        # ADD WORKOUT WITHOUT FOLLOWING PLAN
        # ----------------------------------------------------

        elif choice == "2":

            add_workout()


        # ----------------------------------------------------
        # EXIT
        # ----------------------------------------------------

        elif choice == "3":

            break


        else:

            print(
                "\nInvalid option. "
                "Please choose 1, 2, or 3."
            )

# ============================================================
# PART 12A — BODY WEIGHT MENU
# ============================================================

def body_weight_menu():

    while True:

        print("\n")
        print("##########################################")
        print("#              BODY WEIGHT              #")
        print("##########################################")

        print("\n1. Record Body Weight")
        print("2. View Body Weight History")
        print("3. Delete Weight Entry")
        print("4. Back")


        choice = input(
            "\nChoose option: "
        ).strip()


        if choice == "1":

            record_body_weight()


        elif choice == "2":

            view_body_weight_history()


        elif choice == "3":

            delete_body_weight_entry()


        elif choice == "4":

            break


        else:

            print(
                "\nInvalid option."
            )
            
# ============================================================
# PART 12B — RECORD BODY WEIGHT
# ============================================================

def record_body_weight():

    print("\n")
    print("##########################################")
    print("#         RECORD BODY WEIGHT             #")
    print("##########################################")


    while True:

        weight_input = input(
            "\nEnter your body weight in kg: "
        ).strip()


        try:

            weight = float(weight_input)


            if weight <= 0:

                print(
                    "\nWeight must be greater than 0."
                )

                continue


            save_body_weight(weight)

            break


        except ValueError:

            print(
                "\nPlease enter a valid weight."
            )
# ============================================================
# PART 12C — DELETE BODY WEIGHT ENTRY
# ============================================================

def delete_body_weight_entry():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()


    cursor.execute("""
        SELECT
            weight_id,
            weight,
            recorded_date,
            recorded_time

        FROM body_weight_history

        ORDER BY
            recorded_date DESC,
            recorded_time DESC
    """)


    records = cursor.fetchall()


    if not records:

        conn.close()

        print(
            "\nNo body weight records found."
        )

        return


    print("\n")
    print("##########################################")
    print("#       DELETE BODY WEIGHT ENTRY         #")
    print("##########################################")


    print("\nBody Weight History:")


    for number, record in enumerate(
        records,
        start=1
    ):

        weight_id, weight, date, time = record

        print(
            f"{number}. "
            f"{weight} kg — "
            f"{date} {time}"
        )


    print("\n0. Cancel")


    while True:

        try:

            choice = int(
                input(
                    "\nSelect entry to delete: "
                )
            )


            if choice == 0:

                conn.close()

                print(
                    "\nDeletion cancelled."
                )

                return


            if 1 <= choice <= len(records):

                selected = records[
                    choice - 1
                ]

                weight_id = selected[0]


                confirm = input(
                    "\nDelete this entry? "
                    "(yes/no): "
                ).lower().strip()


                if confirm == "yes":

                    cursor.execute("""
                        DELETE FROM body_weight_history

                        WHERE weight_id = ?
                    """, (weight_id,))


                    conn.commit()

                    print(
                        "\nBody weight entry "
                        "deleted successfully."
                    )

                else:

                    print(
                        "\nDeletion cancelled."
                    )


                conn.close()

                return


            print(
                "\nPlease select a valid entry."
            )


        except ValueError:

            print(
                "\nPlease enter a number."
            )
# ============================================================
# PART 13C — VIEW ALL WORKOUT HISTORY
# ============================================================

def view_workout_history():

    connection = get_database_connection()

    cursor = connection.cursor()


    cursor.execute("""
        SELECT
            id,
            day,
            workout_type,
            workout_date

        FROM workout_sessions

        ORDER BY workout_date DESC
    """)


    sessions = cursor.fetchall()


    if not sessions:

        connection.close()

        print("\nNo workout history found.")

        return


    print("\n")
    print("##########################################")
    print("#           WORKOUT HISTORY              #")
    print("##########################################")


    for session in sessions:

        session_id = session[0]
        day = session[1]
        workout_type = session[2]
        workout_date = session[3]


        print("\n==========================================")

        print(
            f"Date/Time: {workout_date}"
        )

        print(
            f"Day: {day}"
        )

        print(
            f"Workout Type: {workout_type}"
        )

        print("==========================================")


        # ----------------------------------------------------
        # GET EXERCISES FOR THIS SESSION
        # ----------------------------------------------------

        cursor.execute("""
            SELECT
                id,
                exercise_id,
                exercise_name

            FROM performed_exercises

            WHERE session_id = ?

            ORDER BY id
        """, (session_id,))


        exercises = cursor.fetchall()


        for exercise in exercises:

            performed_exercise_id = exercise[0]
            exercise_name = exercise[2]


            print(
                f"\n{exercise_name}"
            )


            # ------------------------------------------------
            # GET SETS
            # ------------------------------------------------

            cursor.execute("""
                SELECT
                    set_number,
                    reps,
                    weight

                FROM performed_sets

                WHERE performed_exercise_id = ?

                ORDER BY set_number
            """, (
                performed_exercise_id,
            ))


            sets = cursor.fetchall()


            for workout_set in sets:

                set_number = workout_set[0]
                reps = workout_set[1]
                weight = workout_set[2]


                print(
                    f"   Set {set_number}: "
                    f"{reps} reps × "
                    f"{weight} kg"
                )


    connection.close()
# ============================================================
# WORKOUT HISTORY MENU
# ============================================================

def workout_history_menu():

    while True:

        print("\n")
        print("##########################################")
        print("#           WORKOUT HISTORY              #")
        print("##########################################")

        print("\n1. View All Workout History")
        print("2. View Today's Workouts")
        print("3. View This Week's Workouts")
        print("4. View This Month's Workouts")
        print("5. Delete Workout History")
        print("6. Back")


        choice = input(
            "\nChoose option: "
        ).strip()


        if choice == "1":
            view_workout_history()

        elif choice == "2":
            view_workout_history_by_period("today")

        elif choice == "3":
            view_workout_history_by_period("week")

        elif choice == "4":
            view_workout_history_by_period("month")

        elif choice == "5":
            delete_workout_history()

        elif choice == "6":
            break

        else:
            print("\nInvalid option.")

        
# ============================================================
# PART 14A — VIEW WORKOUT HISTORY
# ============================================================

def view_workout_history():

    connection = get_database_connection()
    cursor = connection.cursor()

    print("\n")
    print("##########################################")
    print("#          WORKOUT HISTORY              #")
    print("##########################################")

    cursor.execute("""
        SELECT
            id,
            day,
            workout_type,
            workout_date
        FROM workout_sessions
        ORDER BY workout_date DESC
    """)

    sessions = cursor.fetchall()

    if not sessions:

        print("\nNo workout history found.")

        connection.close()

        return


    for session in sessions:

        session_id = session[0]
        day = session[1]
        workout_type = session[2]
        workout_date = session[3]

        print("\n==========================================")

        print(
            f"Workout ID: {session_id}"
        )

        print(
            f"Date/Time: {workout_date}"
        )

        print(
            f"Day: {day}"
        )

        print(
            f"Type: {workout_type}"
        )

        print("==========================================")


        cursor.execute("""
            SELECT
                id,
                exercise_name
            FROM performed_exercises
            WHERE session_id = ?
            ORDER BY id
        """, (session_id,))

        exercises = cursor.fetchall()


        for exercise in exercises:

            performed_exercise_id = exercise[0]
            exercise_name = exercise[1]

            print(
                f"\nExercise: {exercise_name}"
            )


            cursor.execute("""
                SELECT
                    set_number,
                    reps,
                    weight
                FROM performed_sets
                WHERE performed_exercise_id = ?
                ORDER BY set_number
            """, (performed_exercise_id,))


            sets = cursor.fetchall()


            for workout_set in sets:

                set_number = workout_set[0]
                reps = workout_set[1]
                weight = workout_set[2]

                print(
                    f"  Set {set_number}: "
                    f"{reps} reps × "
                    f"{weight} kg"
                )


    connection.close()

# ============================================================
# PART 14B — DELETE WORKOUT HISTORY
# ============================================================

def delete_workout_history():

    connection = get_database_connection()
    cursor = connection.cursor()

    print("\n")
    print("##########################################")
    print("#         DELETE WORKOUT HISTORY        #")
    print("##########################################")


    # --------------------------------------------------------
    # GET ALL WORKOUT SESSIONS
    # --------------------------------------------------------

    cursor.execute("""
        SELECT
            id,
            day,
            workout_type,
            workout_date
        FROM workout_sessions
        ORDER BY workout_date DESC
    """)

    sessions = cursor.fetchall()


    if not sessions:

        print(
            "\nNo workout history found."
        )

        connection.close()

        return


    # --------------------------------------------------------
    # SHOW WORKOUTS
    # --------------------------------------------------------

    print("\nSaved Workouts:")

    for number, session in enumerate(
        sessions,
        start=1
    ):

        session_id = session[0]
        day = session[1]
        workout_type = session[2]
        workout_date = session[3]


        print(
            f"\n{number}. "
            f"{day} | "
            f"{workout_date} | "
            f"{workout_type}"
        )


    print(
        "\n0. Cancel"
    )


    # --------------------------------------------------------
    # SELECT WORKOUT
    # --------------------------------------------------------

    while True:

        try:

            choice = int(
                input(
                    "\nSelect workout to delete: "
                )
            )


            if choice == 0:

                print(
                    "\nDeletion cancelled."
                )

                connection.close()

                return


            if 1 <= choice <= len(sessions):

                break


            print(
                "\nPlease select a valid workout."
            )


        except ValueError:

            print(
                "\nPlease enter a number."
            )


    selected_session = sessions[
        choice - 1
    ]


    session_id = selected_session[0]


    # --------------------------------------------------------
    # CONFIRM DELETION
    # --------------------------------------------------------

    print("\n------------------------------------------")

    print(
        f"Selected workout:"
    )

    print(
        f"Date/Time: {selected_session[3]}"
    )

    print(
        f"Day: {selected_session[1]}"
    )

    print(
        f"Type: {selected_session[2]}"
    )

    print("------------------------------------------")


    confirm = input(
        "\nDelete this entire workout "
        "and all its sets? (yes/no): "
    ).lower().strip()


    if confirm != "yes":

        print(
            "\nDeletion cancelled."
        )

        connection.close()

        return


    # --------------------------------------------------------
    # GET PERFORMED EXERCISES
    # --------------------------------------------------------

    cursor.execute("""
        SELECT id
        FROM performed_exercises
        WHERE session_id = ?
    """, (session_id,))


    performed_exercises = cursor.fetchall()


    # --------------------------------------------------------
    # DELETE PERFORMED SETS
    # --------------------------------------------------------

    for performed_exercise in performed_exercises:

        performed_exercise_id = (
            performed_exercise[0]
        )


        cursor.execute("""
            DELETE FROM performed_sets
            WHERE performed_exercise_id = ?
        """, (performed_exercise_id,))


    # --------------------------------------------------------
    # DELETE PERFORMED EXERCISES
    # --------------------------------------------------------

    cursor.execute("""
        DELETE FROM performed_exercises
        WHERE session_id = ?
    """, (session_id,))


    # --------------------------------------------------------
    # DELETE WORKOUT SESSION
    # --------------------------------------------------------

    cursor.execute("""
        DELETE FROM workout_sessions
        WHERE id = ?
    """, (session_id,))


    # --------------------------------------------------------
    # SAVE DELETION
    # --------------------------------------------------------

    connection.commit()

    connection.close()


    print("\n==========================================")

    print(
        "Workout history deleted successfully."
    )

    print("==========================================")

# ============================================================
# PART 14C — WORKOUT HISTORY MENU
# ============================================================

def workout_history_menu():
    while True:
        print("\n")
        print("##########################################")
        print("#            WORKOUT HISTORY             #")
        print("##########################################")

        print("\n1. View All Workout History")
        print("2. View Today's Workouts")
        print("3. View This Week's Workouts")
        print("4. View This Month's Workouts")
        print("5. Delete Workout History")
        print("6. Back")

        choice = input("\nChoose option: ").strip()

        # ----------------------------------------------------
        # VIEW ALL
        # ----------------------------------------------------
        if choice == "1":
            view_workout_history()

        # ----------------------------------------------------
        # VIEW BY PERIODS
        # ----------------------------------------------------
        elif choice == "2":
            view_workout_history_by_period("today")

        elif choice == "3":
            view_workout_history_by_period("week")

        elif choice == "4":
            view_workout_history_by_period("month")

        # ----------------------------------------------------
        # DELETE
        # ----------------------------------------------------
        elif choice == "5":
            delete_workout_history()

        # ----------------------------------------------------
        # BACK
        # ----------------------------------------------------
        elif choice == "6":
            break

        else:
            print("\nInvalid option.")

# ============================================================
# PART 14D-1 — DATE-BASED WORKOUT HISTORY
# ============================================================

def view_workout_history_by_period(period):
    # Ensure correct datetime imports are active inside this scope to avoid crashes
    from datetime import datetime, timedelta

    connection = get_database_connection()
    cursor = connection.cursor()

    # --------------------------------------------------------
    # DETERMINE DATE RANGE
    # --------------------------------------------------------
    today = datetime.now().date()

    if period == "today":
        start_date = today
        end_date = today

    elif period == "week":
        start_date = today - timedelta(days=today.weekday())
        end_date = today

    elif period == "month":
        start_date = today.replace(day=1)
        end_date = today

    else:
        print("\nInvalid history period.")
        connection.close()
        return

    # --------------------------------------------------------
    # GET WORKOUT SESSIONS
    # --------------------------------------------------------
    cursor.execute("""
        SELECT id, day, workout_type, workout_date 
        FROM workout_sessions 
        WHERE DATE(workout_date) BETWEEN ? AND ? 
        ORDER BY workout_date DESC
    """, (start_date.isoformat(), end_date.isoformat()))

    sessions = cursor.fetchall()

    # --------------------------------------------------------
    # NO RESULTS
    # --------------------------------------------------------
    if not sessions:
        print("\n==========================================")
        if period == "today":
            print("NO WORKOUTS FOUND FOR TODAY")
        elif period == "week":
            print("NO WORKOUTS FOUND THIS WEEK")
        elif period == "month":
            print("NO WORKOUTS FOUND THIS MONTH")
        print("==========================================")
        connection.close()
        return

    # --------------------------------------------------------
    # DISPLAY TITLE
    # --------------------------------------------------------
    print("\n")
    print("==========================================")
    if period == "today":
        print("TODAY'S WORKOUTS")
    elif period == "week":
        print("THIS WEEK'S WORKOUTS")
    elif period == "month":
        print("THIS MONTH'S WORKOUTS")
    print("==========================================")

    # --------------------------------------------------------
    # DISPLAY SESSIONS
    # --------------------------------------------------------
    for session in sessions:
        session_id = session[0]
        day = session[1]
        workout_type = session[2]
        workout_date = session[3]

        print("\n------------------------------------------")
        print(f"Date/Time: {workout_date}")
        print(f"Day: {day}")
        print(f"Type: {workout_type}")
        print("------------------------------------------")

        # ----------------------------------------------------
        # GET EXERCISES
        # ----------------------------------------------------
        cursor.execute("""
            SELECT id, exercise_name 
            FROM performed_exercises 
            WHERE session_id = ? 
            ORDER BY id
        """, (session_id,))

        exercises = cursor.fetchall()

        for exercise in exercises:
            performed_exercise_id = exercise[0]
            exercise_name = exercise[1]

            print(f"\nExercise: {exercise_name}")

            # ------------------------------------------------
            # GET SETS
            # ------------------------------------------------
            cursor.execute("""
                SELECT set_number, reps, weight 
                FROM performed_sets 
                WHERE performed_exercise_id = ? 
                ORDER BY set_number
            """, (performed_exercise_id,))

            sets = cursor.fetchall()

            for workout_set in sets:
                set_number = workout_set[0]
                reps = workout_set[1]
                weight = workout_set[2]

                print(f"  Set {set_number}: {reps} reps × {weight} kg")

    connection.close()
# ============================================================
def run_goal_based_analysis_hub():
    """
    Core Feature Module: Automatically reads the user's active profile goal from the database 
    and runs a specialized, condition-based diagnostic audit on their plan.
    """
    # 1. VERIFY WORKOUT PLAN HAS DATA
    has_exercises = any(WORKOUT_PLAN[day]["exercises"] for day in DAYS)
    if not has_exercises:
        print("\n❌ Your weekly plan is completely empty! Add exercises before running the goal diagnostic.")
        return

    # 2. AUTO-LOAD GOAL FROM DATABASE PROFILE
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT goal FROM user_profile ORDER BY id DESC LIMIT 1")
    profile = cursor.fetchone()
    connection.close()

    db_goal = str(profile["goal"]).lower().strip() if profile else "not set"

    if "hypertrophy" in db_goal or "muscle mass" in db_goal: choice = "1"
    elif "strength" in db_goal: choice = "2"
    elif "fat loss" in db_goal: choice = "3"
    elif "endurance" in db_goal: choice = "4"
    elif "power" in db_goal or "explosiveness" in db_goal: choice = "5"
    else: choice = "6"

    if choice not in ["1", "2"]:
        print(f"\n⏳ Configuration Locked: We are finalizing the logic models for goals 3-6 next.")
        print("Running diagnostic using your profile configuration path...\n")
        return

    # 3. INITIALIZE VARIABLES EXPLICITLY TO PREVENT NAMEERRORS
    muscle_groups_data = {
        "Chest": ["upper_chest", "middle_chest", "lower_chest"],
        "Back": ["lat_width", "upper_back", "lower_back"],
        "Shoulders": ["front_shoulder", "side_shoulder", "rear_shoulder"],
        "Arms": ["biceps_outer", "biceps_inner", "triceps_long", "triceps_outer", "triceps_inner"],
        "Legs": ["quads", "hamstrings", "glutes_main", "glutes_side", "calves_upper", "calves_lower"],
        "Core": ["abs_front", "abs_sides"],
    }

    muscle_frequency = {group: 0 for group in muscle_groups_data}
    weekly_subdivision_volume = {k: 0.0 for bucket in muscle_groups_data.values() for k in bucket}
    
    push_volume = 0.0
    pull_volume = 0.0
    total_sets_checked = 0
    hypertrophy_out_of_range_sets = 0
    strength_range_sets = 0       
    pump_range_sets = 0           
    total_compound_sets = 0
    total_isolation_sets = 0

    active_workout_days_count = 0

    # 4. RUN DATA COMPILATION MATRIX LOOP
    for day in DAYS:
        day_plan = WORKOUT_PLAN.get(day, {})
        planned_exercises = day_plan.get("exercises", [])
        
        if planned_exercises:
            active_workout_days_count += 1
        
        muscles_tracked_today = set()
        for item in planned_exercises:
            ex_id = item["exercise_id"]
            sets = item["sets"]
            reps = item["reps"]
            total_sets_checked += sets

            db_ex = EXERCISES.get(ex_id, {})
            movement_pattern = str(db_ex.get("movement", "")).lower()
            ex_type = str(db_ex.get("type", "Compound")).lower()

            if "isolation" in ex_type: total_isolation_sets += sets
            else: total_compound_sets += sets

            if reps < 8 or reps > 12: hypertrophy_out_of_range_sets += sets
            if 3 <= reps <= 6: strength_range_sets += sets
            elif reps >= 12: pump_range_sets += sets

            if "push" in movement_pattern: push_volume += sets
            elif "pull" in movement_pattern: pull_volume += sets

            distribution = db_ex.get("biometric_distribution", {})
            for head_key, factor in distribution.items():
                if head_key in weekly_subdivision_volume:
                    weekly_subdivision_volume[head_key] += (sets * factor)
                    for group_name, sub_heads in muscle_groups_data.items():
                        if head_key in sub_heads:
                            muscles_tracked_today.add(group_name)

        for group in muscles_tracked_today:
            muscle_frequency[group] += 1

    # ====================================================
    # DIAGNOSTIC PATH 1: HYPERTROPHY 
    # ====================================================
    if choice == "1":
        alignment_score = 100.0
        triggered_alerts = []
        
        MAJOR_GROUPS = ["Chest", "Back", "Shoulders", "Legs"]

        print("\n" + "═" * 45)
        print("🔍   HYPERTROPHY GOAL DIAGNOSTIC REPORT   ")
        print("═" * 45)

        # 1. WEEKLY ACTIVE WORKOUT DAYS AUDIT
        if active_workout_days_count < 4:
            alignment_score -= 20.0
            triggered_alerts.append(
                f"🚨 Frequency Deficit: You are training less than 4 days in a week ({active_workout_days_count} day(s) active) which is not optimal for hypertrophy.\n"
                f"     Instruction: The sweet spot for maximizing muscle mass gains is 5 days a week to distribute volume optimally."
            )

        # 2. ENTIRELY IGNORED/NEGLECTED MAJOR GROUPS (0 Points Deducted Rule)
        ignored_majors = [g for g in MAJOR_GROUPS if muscle_frequency.get(g, 0) == 0]
        if ignored_majors:
            print("📋 Structural Target Advisories (0 Points Deducted):")
            for group in ignored_majors:
                print(f"   -> ⚠️  The {group.lower()} group is under-trained / completely omitted from your active weekly cycle.")
            print("-" * 45)

        # 3. WEEKLY MUSCLE FREQUENCY AUDIT
        for group in MAJOR_GROUPS:
            freq = muscle_frequency.get(group, 0)
            if freq == 1:
                alignment_score -= 10.0
                triggered_alerts.append(
                    f"🔴 Insufficient Muscle Frequency: You are training {group.lower()} only once a week.\n"
                    f"     Instruction: You should train {group.lower()} twice a week according to your goal to trigger muscle protein synthesis optimally."
                )

        # 4. TOTAL WEEKLY SET CAPACITY VOLUME AUDIT
        for group in MAJOR_GROUPS:
            freq = muscle_frequency.get(group, 0)
            if freq > 0:
                sub_heads = muscle_groups_data[group]
                total_weekly_group_sets = sum(weekly_subdivision_volume[h] for h in sub_heads)
                
                if total_weekly_group_sets < 10.0:
                    alignment_score -= 10.0
                    triggered_alerts.append(
                        f"⚠️ Inadequate Weekly Volume: Total sets for {group.lower()} this week is less than 10 ({total_weekly_group_sets:.1f} sets mapped).\n"
                        f"     Instruction: For reliable hypertrophic adaptations, major columns require at least 10 hard working sets per week."
                    )

        # 5. DYNAMIC JOINT BALANCES & REP SCANS
        if total_sets_checked > 0 and (hypertrophy_out_of_range_sets / total_sets_checked) > 0.30:
            alignment_score -= 10.0
            triggered_alerts.append(
                f"重新 Rep Range Deviation: A notable block of sets falls outside the target hypertrophic range.\n"
                f"     Instruction: Configure your exercises to target 8-12 reps per set near failure."
            )

        if pull_volume > 0:
            ratio = push_volume / pull_volume
            if ratio > 1.3 or ratio < 0.7:
                alignment_score -= 5.0
                triggered_alerts.append(
                    f"🚨 Joint Health Warning: Your push-to-pull volume ratio is highly asymmetrical ({push_volume:.1f} vs {pull_volume:.1f} sets).\n"
                    f"     Instruction: To keep shoulder joints stable, aim for a balanced 1:1 setup."
                )

        # RENDER CARD
        final_score = max(10.0, min(100.0, alignment_score))
        print(f"⭐ GOAL ALIGNMENT RATING: {final_score:.1f} / 100")
        print("═" * 45)

        if triggered_alerts:
            print("\n📋 REQUIRED COGNITIVE CALIBRATIONS:")
            for idx, alert in enumerate(triggered_alerts, start=1):
                print(f"\n{idx}. {alert}")
        else:
            print("\n✅ Flawless Configuration: Your routine structure perfectly satisfies your active mass targets.")

        print("\n💡 ESSENTIAL EXECUTION INSIGHT:")
        print("   -> You should reach absolute physical failure per set with only 1-2 reps left in reserve (RIR).\n"
              "   -> If these are low-effort, casual volume sets, you may not get any muscle growth results.")
        print("═" * 45)

    # ====================================================
    # DIAGNOSTIC PATH 2: STRENGTH GAIN
    # ====================================================
    elif choice == "2":
        alignment_score = 100.0
        triggered_alerts = []

        print("\n" + "═" * 45)
        print("🔍   STRENGTH GAIN DIAGNOSTIC REPORT   ")
        print("═" * 45)

        if total_sets_checked > 0 and (strength_range_sets / total_sets_checked) < 0.40:
            alignment_score -= 20.0
            triggered_alerts.append(
                f"⚠️  Intensity Allocation Low: Your plan lacks primary strength-building loading zones.\n"
                f"     Instruction: To build true maximal strength, your main heavy structural lifts should target 3-6 reps at roughly 85-90% of your one-rep max (1RM)."
            )

        print("📌 Target Rest Notice: Rest 2–5 minutes on main compounds to allow complete central nervous system (CNS) neurological recovery.")

        if total_sets_checked > 0:
            isolation_ratio = total_isolation_sets / total_sets_checked
            if isolation_ratio > 0.40:
                alignment_score -= 15.0
                triggered_alerts.append(
                    f"🔴 Excessive Isolation Volume: Isolation movements account for {isolation_ratio*100:.1f}% of your program.\n"
                    f"     Instruction: For maximum strength gain, heavy compound multi-joint movements must dominate your routine. Reduce isolation work below 40%."
                )


# PART 4 — MAIN WORKOUT PLAN BUILDER MENU
# ============================================================
def workout_plan_builder():

    print("\n")
    print("##########################################")
    print("#      WORKOUT PLAN BUILDER              #")
    print("##########################################")


    while True:
        print("\n==========================================")
        print("PLAN BUILDER MENU")
        print("==========================================")
        print("1. Select Day & Edit Routine")
        print("2. 📊 Run Scientific Volume Analysis")
       # print("3. 🎯 Check Analysis Based on Your Workout Goal")
        print("3. Back to Main Menu")

        choice = input("\nChoose option: ").strip()

        # Routes directly to your smart analysis hub function
        if choice == "2":
            analyze_planned_workout_routine()
            continue

        elif choice == "3":
        	return
        
        #elif choice == "3":
           
           # run_goal_based_analysis_hub()
         #   continue

        elif choice == "1":
            day = select_day()
            
            if day is None:
                continue

            if (day in WORKOUT_PLAN and WORKOUT_PLAN[day]["body_parts"]):
                manage_day(day)
            else:
                build_day(day)

            another_day = input("\nModify another day? (yes/no): ").lower().strip()
            if another_day != "yes":
                break
        else:
            print("\nInvalid option. Please choose 1, 2, or 3.")


    print("\n")
    print("##########################################")
    print("#      CURRENT WEEKLY PLAN               #")
    print("##########################################")

    for day in DAYS:
        show_day_plan(day)


#@@@@@@@@@@@@@@@@
         #MAIN MENUE
#@@@@@@@@@@@@@####


def main_menu():
    while True:
        print("\n")
        print("##########################################")
        print("#             FITNESS APP                #")
        print("##########################################")
        print("1. View/Update Weekly Plan")
        print("2. Start Workout")
        print("3. Setup/Edit User Profile")
        print("4. Body Weight")
        print("5. Workout History")
        print("6. Exit")
        
        choice = input("\nChoose option: ").strip()
        
        if choice == "1":
            workout_plan_builder()
        elif choice == "2":
            start_workout_menu()
        elif choice == "3":
            create_profile_interface()
        elif choice == "4":
            body_weight_menu()
        elif choice == "5":
        	workout_history_menu()
        elif choice == "6":
            print("\nExiting application. Keep crushing it!")
            break
        else:
            print("\nInvalid option. Please choose 1, 2, 3, 4, 5 or 6.")



# ============================================================
# APPLICATION INITIALIZATION
# ============================================================

# ============================================================
# DATABASE INITIALIZATION
# ============================================================

initialize_database()
initialize_plan_database()
create_workout_history_tables()
create_body_weight_table()
load_workout_plan()
# ============================================================
# START APPLICATION
# ============================================================

main_menu()