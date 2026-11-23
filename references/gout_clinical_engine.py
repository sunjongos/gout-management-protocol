from dataclasses import dataclass
from typing import Dict, List, Any


@dataclass
class GoutClinicalAssessment:
    stage: str
    target_sua: float
    current_sua: float
    sua_gap: float
    acute_management: List[str]
    chronic_ult_plan: List[str]
    lifestyle_prescriptions: List[str]
    contraindication_alerts: List[str]


def evaluate_gout_patient(
    current_sua: float,
    is_acute_flare: bool,
    flare_count_past_year: int,
    has_tophi: bool,
    on_existing_ult: bool,
    drinks_alcohol: bool,
    frequent_beer: bool,
    frequent_fructose_soda: bool,
    bmi: float,
    crash_dieting: bool,
) -> GoutClinicalAssessment:
    alerts = []
    acute_plan = []
    chronic_plan = []
    lifestyle = []

    if is_acute_flare:
        stage = "급성 통풍 관절염 발작기 (Acute Gout Flare)"
    elif has_tophi:
        stage = "만성 결절성 통풍 (Chronic Tophaceous Gout)"
    elif flare_count_past_year > 0:
        stage = "간헐기 통풍 (Intercritical Gout)"
    else:
        stage = "무증상 고요산혈증 (Asymptomatic Hyperuricemia)"

    target_sua = 5.0 if has_tophi else 6.0
    sua_gap = round(current_sua - target_sua, 2)

    if is_acute_flare:
        acute_plan.append("1차 약제: 강력 소염진통제(NSAIDs, 예: 나프록센) 또는 저용량 콜키신(초기 1.2mg 후 1시간 뒤 0.6mg).")
        acute_plan.append("보조 처치: 환부 다리 거상(Elevation) 및 얼음찜질(Ice pack).")
        if not on_existing_ult:
            alerts.append("[절대 금기] 급성 발작 중 요산저하제(페브릭/자이로릭) 신규 투여 금지! 결정 표면 교란으로 발작 악화 위험.")
            acute_plan.append("요산저하제는 발작이 완전히 가라앉은 2~4주 후부터 저용량으로 시작하십시오.")
        else:
            acute_plan.append("[유지] 기존 복용 중이던 요산저하제는 용량 변경 없이 그대로 유지하십시오.")

    requires_ult = flare_count_past_year >= 2 or has_tophi or current_sua >= 9.0
    if requires_ult:
        chronic_plan.append(f"목표 요산 수치: {target_sua} mg/dL 이하 영구 유지 (현재 {current_sua} mg/dL, {sua_gap:+.1f} mg/dL 조절 필요).")
        chronic_plan.append("1차 추천 약제: Febuxostat(페브릭) 40mg -> 필요 시 80mg 증량 (신기능 저하 환자에서도 상대적 안전).")
        chronic_plan.append("Allopurinol(자이로릭) 사용 시 한국인 중증피부약물유해반응(SCARs) 예방을 위한 HLA-B*5801 유전자 검사 권장.")
        chronic_plan.append("플레어 예방 요법: 요산제 시작 초기 3~6개월간 저용량 콜키신(0.6mg 1일 1회) 병용 필수.")
    else:
        chronic_plan.append("현재는 연 2회 이상 발작이 없으므로 철저한 생활습관 교정과 정기 sUA 추적 관찰을 우선합니다.")

    if frequent_beer or drinks_alcohol:
        lifestyle.append("[음주 엄단] 맥주는 퓨린 함량이 높고, 알코올 대사산물인 젖산(Lactate)이 신장의 요산 배설을 강력히 억제하므로 금주하십시오.")
    if frequent_fructose_soda:
        lifestyle.append("[과당 차단] 액상과당 음료는 간 내 ATP를 급격히 고갈시켜 퓨린 분해를 폭증시키므로 물/탄산수로 대체하십시오.")
    if bmi >= 25.0:
        lifestyle.append(f"[체중 감량 제1원칙] 현재 BMI {bmi:.1f}. 단순 퓨린 제한보다 총 칼로리를 줄여 체중을 감량하는 것이 요산 강하에 훨씬 효과적입니다.")
    if crash_dieting:
        alerts.append("[발작 경보] 극단적 단식이나 급격한 체중 감량은 요산 수치의 급변동을 일으켜 통풍 발작을 유발합니다. 월 1~2kg 완만한 감량을 유지하십시오.")

    lifestyle.append("[수분 섭취] 하루 2L 이상 충분한 수분을 섭취하여 요산을 희석하고 소변 배출을 유도하십시오.")
    lifestyle.append("[식물성 식품 안심] 콩, 두부, 버섯, 시금치 등 식물성 퓨린은 통풍 위험을 높이지 않으므로 영양을 위해 안심하고 섭취하십시오.")

    return GoutClinicalAssessment(
        stage=stage,
        target_sua=target_sua,
        current_sua=current_sua,
        sua_gap=sua_gap,
        acute_management=acute_plan,
        chronic_ult_plan=chronic_plan,
        lifestyle_prescriptions=lifestyle,
        contraindication_alerts=alerts,
    )