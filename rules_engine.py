"""
Author: Snehal Patil
Roll Number: 25101A2002
Project: DHANYARAKSHAK - AI-Powered Ginger Crop Disease Detection
Context: Smart Agriculture & Responsible AI for Social Good
Module: Rule-Based Decision & Advisory Engine
"""

from typing import Dict, Any, Optional

# Comprehensive Agricultural Knowledge Base for Ginger Crops (Zingiber officinale)
GINGER_DISEASE_RULES: Dict[str, Dict[str, Any]] = {
    "Healthy": {
        "scientific_name": "Zingiber officinale (Healthy Foliage)",
        "severity": "Optimal",
        "severity_color": "#28a745",
        "status_summary": "The ginger canopy exhibits vibrant green leaf tissue, healthy venation, and no signs of bacterial or fungal infection.",
        "symptoms": [
            "Uniform emerald green coloration across leaf lamina",
            "Intact leaf margins without necrosis, chlorosis, or curling",
            "Firm, erect pseudostems with robust vascular integrity",
            "No rhizome or collar region water-soaking"
        ],
        "targeted_irrigation": {
            "strategy": "Precision Drip Irrigation & Moisture Conservation",
            "soil_moisture_target": "60% - 70% Field Capacity",
            "water_schedule": "Provide 4-5 mm daily water requirement via root-zone emitters during peak vegetative stage.",
            "conservation_tip": "Apply organic mulch (dry paddy straw or silver oak leaves @ 10-12 tons/ha). This reduces soil evaporation by up to 40% and regulates rhizosphere temperature."
        },
        "recommended_treatment": {
            "chemical": "No chemical pesticide intervention required. Maintain standard micronutrient foliar spray (Zinc Sulfate 0.2% + Borax 0.1%) at 60 and 90 days after planting.",
            "dosage": "Zinc Sulfate 2 g/L, Borax 1 g/L"
        },
        "organic_bio_control": {
            "approach": "Prophylactic Bio-Stimulation & Soil Health",
            "agents": [
                "Prophylactic foliar spray of Neem Seed Kernel Extract (NSKE 5%) every 25-30 days",
                "Apply Panchagavya (3% foliar spray) or Jeevamrutha to stimulate beneficial phyllosphere microbes",
                "Soil inoculation with Azospirillum and Phosphobacteria (20 g/kg rhizome seed)"
            ]
        },
        "preventive_measures": [
            "Maintain deep inter-bed drainage channels (30 cm depth) ahead of monsoon downpours",
            "Inspect field weekly following the DHANYARAKSHAK scouting pattern",
            "Avoid excessive synthetic nitrogenous fertilizers which attract succulent-tissue pests"
        ],
        "water_conservation_impact": "Conserves ~35-40% water compared to conventional flood furrow irrigation through precision moisture pacing.",
        "action_timeline": {
            "Immediate (Day 1-2)": "Maintain current drip schedule and check soil probe readings.",
            "Week 1-2": "Replenish organic leaf mulch cover over bare rhizome mounds.",
            "Monthly": "Apply bio-organic growth booster and continue regular crop scouting."
        }
    },
    "Bacterial Wilt": {
        "scientific_name": "Ralstonia solanacearum (Bacterial Vascular Wilt)",
        "severity": "Critical",
        "severity_color": "#dc3545",
        "status_summary": "High-urgency vascular bacterial invasion. Pathogen colonizes xylem vessels, triggering rapid wilting, bronze curling, and vascular collapse.",
        "symptoms": [
            "Bronze-green upward curling along leaf margins leading to rapid drooping",
            "Pseudostem base shows water-soaked dark brown discoloration",
            "Milky white bacterial ooze flows when cut stem is immersed in clear water (Ooze Test positive)",
            "Rapid plant collapse without preliminary chlorosis (yellowing)"
        ],
        "targeted_irrigation": {
            "strategy": "Immediate Surface Water Lockdown & Isolation Drainage",
            "soil_moisture_target": "Reduce moisture to 45% - 50% to inhibit anaerobic bacterial motility",
            "water_schedule": "Immediately cease flood and overhead irrigation across the entire block. Bacterial flagella spread rapidly via free water films.",
            "conservation_tip": "Isolate the infected bed by excavating 40 cm deep perimeter isolation trenches. Redirect drip lines away from infected root basins to prevent pathogen movement."
        },
        "recommended_treatment": {
            "chemical": "Strict perimeter soil drenching with Streptocycline (antibiotic) + Copper Oxychloride (bactericide).",
            "dosage": "Streptocycline @ 2 g / 10 L water + Copper Oxychloride 50% WP @ 2.5 g / L. Drench 250-500 ml per plant basin."
        },
        "organic_bio_control": {
            "approach": "Microbial Antagonism & Soil Alkalinization",
            "agents": [
                "Soil drenching around boundary zones with Pseudomonas fluorescens (20 g/L, 2.5 kg/ha in 500 L water)",
                "Apply agricultural lime or bleaching powder @ 20-25 kg/ha into isolated infected zones to alter soil pH and suppress bacteria",
                "Foliar spray of Bacillus amyloliquefaciens / Bacillus subtilis strain formulations"
            ]
        },
        "preventive_measures": [
            "Carefully rogue out and incinerate infected ginger clumps; sterilize the soil pit with 2% bleaching powder",
            "Strictly avoid cultivating ginger, tomato, eggplant, or potato in the same plot for at least 3 years",
            "Disinfect farm implements with 70% alcohol or 1% sodium hypochlorite between rows"
        ],
        "water_conservation_impact": "Halting indiscriminate flood irrigation and switching to precision containment conserves critical water while arresting bacterial spread.",
        "action_timeline": {
            "Immediate (Hour 0-24)": "Uproot infected clumps, incinerate off-field, and drench pit with bleaching powder solution.",
            "Day 2-4": "Apply Streptocycline + Copper Oxychloride drench to all plants within a 5-meter buffer perimeter.",
            "Day 7-14": "Apply Pseudomonas fluorescens bio-protectant to buffer rows; re-verify water drainage channels."
        }
    },
    "Leaf Spot": {
        "scientific_name": "Phyllosticta zingiberi (Phyllosticta Leaf Spot / Blight)",
        "severity": "Moderate",
        "severity_color": "#ffc107",
        "status_summary": "Foliar fungal infection causing progressive necrotic spotting, reduction in photosynthetic leaf area, and premature senescence.",
        "symptoms": [
            "Minute oval to circular yellowish spots on upper leaf surface",
            "Spots enlarge with bleached white or creamy centers and distinct dark brown margins",
            "Multiple spots coalesce causing extensive foliar scorching and papery leaf texture",
            "Pinhead-sized dark pycnidia visible in the center of mature lesions"
        ],
        "targeted_irrigation": {
            "strategy": "Microclimate Canopy Humidity Suppression & Low-Trajectory Watering",
            "soil_moisture_target": "55% - 65% Field Capacity",
            "water_schedule": "Irrigate solely during early morning hours via ground-level drip emitters. Avoid late afternoon or night watering.",
            "conservation_tip": "Never use overhead sprinklers. Leaf wetness lasting over 3-4 hours stimulates Phyllosticta conidia germination. Drip saves 40% water while keeping leaves dry."
        },
        "recommended_treatment": {
            "chemical": "Foliar fungicide application targeting both contact protection and systemic translocation.",
            "dosage": "Mancozeb 75% WP @ 2.5 g/L or Carbendazim 50% WP @ 1 g/L or Hexaconazole 5% SC @ 1 ml/L. Spray thoroughly on both leaf surfaces."
        },
        "organic_bio_control": {
            "approach": "Protective Copper Barrier & Bio-Fungicide",
            "agents": [
                "Foliar spray of freshly prepared Bordeaux Mixture (1%: 1 kg Copper Sulfate + 1 kg Quicklime in 100 L water)",
                "Foliar bio-fungicide: Trichoderma viride liquid formulation @ 5 ml/L",
                "Cold-pressed Neem Oil (3 ml/L) combined with mild potassium soap as an eco-friendly spreader"
            ]
        },
        "preventive_measures": [
            "Manually collect and compost/burn severely blighted leaves to reduce fungal spore load",
            "Maintain optimal row spacing (25-30 cm) to ensure adequate airflow and sunlight through the crop canopy",
            "Apply potassium sulfate (K2SO4) foliar nutrition (0.5%) to strengthen leaf epidermal cell walls"
        ],
        "water_conservation_impact": "Eliminating overhead sprinkler runoffs and confining water to drip emitters reduces fungal spread and saves 30-40% water.",
        "action_timeline": {
            "Day 1-2": "Spray 1% Bordeaux mixture or Mancozeb 75% WP across affected rows and adjacent buffer beds.",
            "Day 5-7": "Prune heavily necrosed leaves; verify that drip lines are not wetting lower foliage.",
            "Day 14": "Apply follow-up systemic fungicide (Carbendazim or Hexaconazole) if new lesions emerge."
        }
    },
    "Soft Rot": {
        "scientific_name": "Pythium aphanidermatum / Pythium myriotylum (Rhizome Soft Rot)",
        "severity": "High",
        "severity_color": "#fd7e14",
        "status_summary": "Extremely devastating oomycete/fungal complex causing water-soaked collar rot and liquefied decomposition of seed and daughter rhizomes.",
        "symptoms": [
            "Progressive chlorosis (yellowing) starting from margins of lowest leaves and advancing upward",
            "Pseudostem collar at ground level becomes soft, glassy, water-soaked, and easily pulls away with a gentle tug",
            "Rotting rhizome develops foul odor, loses internal turgidity, and turns to a brownish pulpy decay",
            "Complete lodging (falling over) of infected tillers"
        ],
        "targeted_irrigation": {
            "strategy": "Aggressive Aeration & Strict Anti-Waterlogging Drainage",
            "soil_moisture_target": "50% - 55% Field Capacity (Avoid soil saturation)",
            "water_schedule": "Suspend irrigation for 48-72 hours if saturated. Transition to pulsed micro-drip cycles (15-20 min cycles) to ensure aerobic conditions.",
            "conservation_tip": "Form 20 cm raised planting beds separated by 35 cm deep drainage runnels. Standing water is the #1 vector for Pythium zoospores."
        },
        "recommended_treatment": {
            "chemical": "Immediate collar and bed drenching with specialized anti-oomycete systemic fungicides.",
            "dosage": "Metalaxyl-Mancozeb (Ridomil MZ 72 WP @ 2.5 g/L) or Fosetyl-Aluminium (Aliette 80 WP @ 2 g/L) or Copper Oxychloride 50 WP @ 3 g/L. Apply 3-5 L/sq. meter."
        },
        "organic_bio_control": {
            "approach": "Rhizosphere Antagonistic Inoculation & Organic Amendments",
            "agents": [
                "Soil incorporation of Trichoderma harzianum enriched in well-cured vermicompost/FYM (2.5 kg Trichoderma in 50 kg FYM per 1000 sq. meters)",
                "Neem Cake soil incorporation @ 200 kg/acre to suppress soil-borne Pythium and plant-parasitic nematodes",
                "Rhizome seed pre-treatment with Trichoderma viride (10 g/kg seed) before planting"
            ]
        },
        "preventive_measures": [
            "Never harvest or plant ginger in waterlogged, heavy clay soil without incorporating sand and compost",
            "Practice solarization of raised nursery beds with clear polythene sheets (40-gauge) during summer for 30-40 days",
            "Implement crop rotation with maize, sorghum, or sunn hemp; avoid rotating with solanaceous crops"
        ],
        "water_conservation_impact": "Pulsed micro-drip combined with raised bed drainage prevents destructive root flooding, conserving 45% water compared to basin irrigation.",
        "action_timeline": {
            "Immediate (Day 1)": "Stop watering; open clogged drainage ditches; rogue out collapsed plants with surrounding soil.",
            "Day 2-3": "Drench plant bases with Metalaxyl-Mancozeb (Ridomil MZ @ 2.5 g/L).",
            "Day 10-14": "Apply Trichoderma harzianum fortified compost around surviving clumps to rebuild soil biology."
        }
    },
    "Anthracnose": {
        "scientific_name": "Colletotrichum capsici / Fusarium oxysporum (Anthracnose / Leaf Blight)",
        "severity": "Moderate to High",
        "severity_color": "#e83e8c",
        "status_summary": "Foliar and sheath anthracnose causing sunken dark necrotic lesions, leaf tip dieback, and stunted rhizome expansion.",
        "symptoms": [
            "Sunken, round to elliptical dark brown spots with prominent yellow halos on leaf blades",
            "Concentric rings of tiny black acervuli within dry necrotic centers",
            "Dieback of leaf tips progressing inward along the midrib",
            "Premature defoliation resulting in severe photosynthetic yield penalty"
        ],
        "targeted_irrigation": {
            "strategy": "Evapotranspiration-Guided Precision Drip",
            "soil_moisture_target": "60% Field Capacity",
            "water_schedule": "Deliver water based on real-time crop evapotranspiration (ETc) demand. Irrigate at dawn so morning warmth quickly evaporates residual humidity.",
            "conservation_tip": "Install drip sensors to eliminate over-irrigation. Maintaining a balanced canopy humidity below 75% inhibits Colletotrichum sporulation."
        },
        "recommended_treatment": {
            "chemical": "Targeted strobilurin or triazole systemic foliar fungicide.",
            "dosage": "Azoxystrobin 23% SC @ 1 ml/L or Difenoconazole 25% EC @ 0.75 ml/L or Propiconazole 25% EC @ 1 ml/L. Repeat after 14 days if needed."
        },
        "organic_bio_control": {
            "approach": "Botanical Fungicides & Microbial Shielding",
            "agents": [
                "Cow urine + fermented neem leaf decoction (1:10 dilution) sprayed as an organic anti-fungal barrier",
                "Foliar spray of Pseudomonas fluorescens (5 g/L) + skimmed milk (1 ml/L as adhesive sticker)",
                "Garlic-chili botanical extract spray (2%) for natural fungistatic action"
            ]
        },
        "preventive_measures": [
            "Use certified disease-free, plump seed rhizomes from authenticated seed farms",
            "Avoid excessive chemical nitrogen; supplement with balanced Potassium and Silica to harden cell walls",
            "Maintain clean borders free of wild zingiberaceous weed hosts"
        ],
        "water_conservation_impact": "ETc-guided drip application delivers optimal hydration directly to root zones, saving up to 35% water while suppressing humid disease microclimates.",
        "action_timeline": {
            "Day 1-2": "Apply Azoxystrobin or Difenoconazole foliar spray across affected blocks.",
            "Day 7": "Inspect new leaf growth; clear diseased fallen leaf debris from furrow channels.",
            "Day 14": "Apply organic bio-agent (Pseudomonas fluorescens) as a rotational shield."
        }
    }
}


def get_disease_advisory(
    predicted_class: str,
    confidence_score: float,
    soil_moisture: Optional[float] = None,
    weather_condition: Optional[str] = None
) -> Dict[str, Any]:
    """
    Evaluates model prediction and contextual parameters through the rule-based decision engine,
    generating customized agricultural, water conservation, and treatment advice.

    Parameters:
        predicted_class (str): Disease label output from ResNet50 model pipeline.
        confidence_score (float): Probability score of the top prediction (0.0 to 1.0).
        soil_moisture (Optional[float]): Estimated or measured percentage (0 to 100%).
        weather_condition (Optional[str]): E.g., 'Humid/Rainy', 'Hot/Dry', 'Moderate'.

    Returns:
        Dict[str, Any]: Structured advisory with actionable recommendations, water conservation rules,
                        and Responsible AI validation indicators.
    """
    # Normalize class name lookup
    matched_class = None
    for key in GINGER_DISEASE_RULES.keys():
        if key.lower() in predicted_class.lower() or predicted_class.lower() in key.lower():
            matched_class = key
            break

    if not matched_class:
        matched_class = "Healthy"  # Safe fallback default

    base_rule = GINGER_DISEASE_RULES[matched_class]

    # Contextual adjustments based on field sensor inputs
    dynamic_advisories = []
    if soil_moisture is not None:
        if soil_moisture > 75.0 and matched_class in ["Soft Rot", "Bacterial Wilt"]:
            dynamic_advisories.append(
                f"CRITICAL WATER ALERT: Current soil moisture is high ({soil_moisture:.1f}%). "
                f"Immediately open perimeter drainage channels to relieve saturation and curb zoospore mobility."
            )
        elif soil_moisture < 50.0 and matched_class == "Healthy":
            dynamic_advisories.append(
                f"IRRIGATION ADVICE: Soil moisture ({soil_moisture:.1f}%) is below optimal field capacity (60-70%). "
                f"Schedule a 30-minute drip cycle during early morning."
            )

    if weather_condition:
        if "rain" in weather_condition.lower() or "humid" in weather_condition.lower():
            if matched_class in ["Leaf Spot", "Anthracnose"]:
                dynamic_advisories.append(
                    f"WEATHER ALERT: High ambient humidity elevates spore dissemination risk. "
                    f"Prioritize protective Bordeaux mixture (1%) or Mancozeb spray immediately after rainfall ceases."
                )

    # Responsible AI Confidence Grading & Guidance
    if confidence_score >= 0.85:
        confidence_tier = "High Confidence"
        confidence_guidance = (
            "The model exhibits high certainty based on distinctive leaf visual pathology. "
            "Proceed with recommended targeted agronomic actions."
        )
    elif confidence_score >= 0.65:
        confidence_tier = "Moderate Confidence"
        confidence_guidance = (
            "The model is moderately confident. Inspect for complementary symptoms (e.g. rhizome collar condition, "
            "ooze test, or lower canopy leaf spot patterns) before heavy chemical application."
        )
    else:
        confidence_tier = "Low Confidence / Ambiguous"
        confidence_guidance = (
            "The model detected ambiguous visual patterns. Consult a local agricultural extension officer (Krishi Vigyan Kendra) "
            "and cross-reference physical leaf samples before initiating chemical interventions."
        )

    return {
        "disease_name": matched_class,
        "scientific_name": base_rule["scientific_name"],
        "severity": base_rule["severity"],
        "severity_color": base_rule["severity_color"],
        "status_summary": base_rule["status_summary"],
        "symptoms": base_rule["symptoms"],
        "targeted_irrigation": base_rule["targeted_irrigation"],
        "recommended_treatment": base_rule["recommended_treatment"],
        "organic_bio_control": base_rule["organic_bio_control"],
        "preventive_measures": base_rule["preventive_measures"],
        "water_conservation_impact": base_rule["water_conservation_impact"],
        "action_timeline": base_rule["action_timeline"],
        "dynamic_advisories": dynamic_advisories,
        "confidence_score": confidence_score,
        "confidence_tier": confidence_tier,
        "confidence_guidance": confidence_guidance,
        "sustainable_score": 92 if matched_class == "Healthy" else 85
    }


def list_supported_diseases():
    """Returns the list of supported ginger crop health categories."""
    return list(GINGER_DISEASE_RULES.keys())
