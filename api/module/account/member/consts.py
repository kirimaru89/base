class Ethnic:
    E1 = 1
    E2 = 2
    E3 = 3
    E4 = 4
    E5 = 5
    E6 = 6
    E7 = 7
    E8 = 8
    E9 = 9
    E10 = 10
    E11 = 11
    E12 = 12
    E13 = 13
    E14 = 14
    E15 = 15
    E16 = 16
    E17 = 17
    E18 = 18
    E19 = 19
    E20 = 20
    E21 = 21
    E22 = 22
    E23 = 23
    E24 = 24
    E25 = 25
    E26 = 26
    E27 = 27
    E28 = 28
    E29 = 29
    E30 = 30
    E31 = 31
    E32 = 32
    E33 = 33
    E34 = 34
    E35 = 35
    E36 = 36
    E37 = 37
    E38 = 38
    E39 = 39
    E40 = 40
    E41 = 41
    E42 = 42
    E43 = 43
    E44 = 44
    E45 = 45
    E46 = 46
    E47 = 47
    E48 = 48
    E49 = 49
    E50 = 50
    E51 = 51
    E52 = 52
    E53 = 53
    E54 = 54
    E55 = 55
    E56 = 56
    E57 = 57
    E58 = 58
    E59 = 59
    E60 = 60
    E61 = 61
    E62 = 62


ETHNIC_CHOICES = (
    (Ethnic.E1, "Kinh"),
    (Ethnic.E2, "Mường"),
    (Ethnic.E3, "Ê đê"),
    (Ethnic.E4, "Thổ"),
    (Ethnic.E5, "Tày"),
    (Ethnic.E6, "Ra Glai"),
    (Ethnic.E7, "Nùng"),
    (Ethnic.E8, "Bố Y"),
    (Ethnic.E9, "Lào"),
    (Ethnic.E10, "Thái"),
    (Ethnic.E11, "Mông"),
    (Ethnic.E12, "Giáy"),
    (Ethnic.E13, "Chăm"),
    (Ethnic.E14, "Lự"),
    (Ethnic.E15, "Dao"),
    (Ethnic.E16, "Mèo"),
    (Ethnic.E17, "Mnông"),
    (Ethnic.E18, "Sán Chay"),
    (Ethnic.E19, "Jrai"),
    (Ethnic.E20, "Cờ Lao"),
    (Ethnic.E21, "La Chí"),
    (Ethnic.E22, "La Ha"),
    (Ethnic.E23, "Pu Péo"),
    (Ethnic.E24, "Ba Na"),
    (Ethnic.E25, "Brâu"),
    (Ethnic.E26, "Bru - Vân Kiều"),
    (Ethnic.E27, "Chơ Ro"),
    (Ethnic.E28, "Cơ Ho"),
    (Ethnic.E29, "Cơ Tu"),
    (Ethnic.E30, "Gỉe Triêng"),
    (Ethnic.E31, "Hrê"),
    (Ethnic.E32, "Kháng"),
    (Ethnic.E33, "Khơ Me"),
    (Ethnic.E34, "Khơ Mú"),
    (Ethnic.E35, "Mạ"),
    (Ethnic.E36, "Mảng"),
    (Ethnic.E37, "Ơ Đu"),
    (Ethnic.E38, "Rơ Măm"),
    (Ethnic.E39, "Tà Ôi"),
    (Ethnic.E40, "Xinh Mun"),
    (Ethnic.E41, "Xinh Mun"),
    (Ethnic.E42, "Xơ Đăng"),
    (Ethnic.E43, "S Tiêng"),
    (Ethnic.E44, "Pà Thẻn"),
    (Ethnic.E45, "Chu Ru"),
    (Ethnic.E46, "Hoa"),
    (Ethnic.E47, "Ngái"),
    (Ethnic.E48, "Sán Dìu"),
    (Ethnic.E49, "Cống"),
    (Ethnic.E50, "Hà Nhì"),
    (Ethnic.E51, "La Hủ"),
    (Ethnic.E52, "Lô Lô"),
    (Ethnic.E53, "Phú Lá"),
    (Ethnic.E54, "Si La"),
    (Ethnic.E55, "Co"),
    (Ethnic.E56, "Sán Chỉ"),
    (Ethnic.E57, "T’Rin"),
    (Ethnic.E58, "Cadong"),
    (Ethnic.E59, "Chứt"),
    (Ethnic.E60, "Jarai"),
    (Ethnic.E61, "Không xác định"),
    (Ethnic.E62, "Cao Lan"),
)

ETHNIC_DIC = dict(ETHNIC_CHOICES)

ETHNICS = [{"value": k, "label": v} for k, v in ETHNIC_CHOICES]


class Religion:
    TL = 1
    K = 2
    CD = 3
    CG = 4
    PG = 5
    HH = 6
    HG = 7
    BH = 8
    BLM = 9
    DTAHN = 10
    TDCS = 11
    BSKH = 12
    MSD = 13
    MLD = 14


RELIGION_CHOICES = (
    (Religion.TL, "Tin Lành"),
    (Religion.K, "Không"),
    (Religion.CD, "Cao Đài"),
    (Religion.CG, "Công giáo"),
    (Religion.PG, "Phật giáo"),
    (Religion.HH, "Hòa Hảo"),
    (Religion.HG, "Hồi giáo"),
    (Religion.BH, "Bahá'í"),
    (Religion.BLM, "Bà La Môn"),
    (Religion.DTAHN, "Đạo Tứ ấn hiếu nghĩa"),
    (Religion.TDCS, "Tịnh độ cư sĩ Phật hội Việt Nam"),
    (Religion.BSKH, "Bửu sơn Kỳ hương"),
    (Religion.MSD, "Minh Sư Đạo"),
    (Religion.MLD, "Minh Lý Đạo"),
)

RELIGION_DIC = dict(RELIGION_CHOICES)

RELIGIONS = [{"value": k, "label": v} for k, v in RELIGION_CHOICES]


class EducationLevel:
    TH = 1
    THCS = 2
    THPT = 3
    HE12 = 4


EDUCATION_LEVEL_CHOICES = (
    (EducationLevel.TH, "Tiểu học"),
    (EducationLevel.THCS, "Trung học cơ sở"),
    (EducationLevel.THPT, "Trung học phổ thông hệ 10/10"),
    (EducationLevel.HE12, "Hệ 12/12"),
)

EDUCATION_LEVEL_DIC = dict(EDUCATION_LEVEL_CHOICES)

EDUCATION_LEVELS = [{"value": k, "label": v} for k, v in EDUCATION_LEVEL_CHOICES]


class Qualification:
    SC = 1
    TC = 2
    CD = 3
    CN = 4
    MA = 5
    DT = 6


QUALIFICATION_CHOICES = (
    (Qualification.SC, "Sơ cấp"),
    (Qualification.TC, "Trung cấp chuyên nghiệp"),
    (Qualification.CD, "Cao đẳng"),
    (Qualification.CN, "Cử nhân"),
    (Qualification.MA, "Thạc sĩ"),
    (Qualification.DT, "Tiến sĩ"),
)

QUALIFICATION_DIC = dict(QUALIFICATION_CHOICES)

QUALIFICATIONS = [{"value": k, "label": v} for k, v in QUALIFICATION_CHOICES]


class ItLevel:
    BASIC = 1
    ADVANCED = 2


IT_LEVEL_CHOICES = (
    (ItLevel.BASIC, "Chuẩn kỹ năng sử dụng CNTT cơ bản"),
    (ItLevel.ADVANCED, "Chuẩn kỹ năng sử dụng CNTT nâng cao"),
)

IT_LEVEL_DIC = dict(IT_LEVEL_CHOICES)

IT_LEVELS = [{"value": k, "label": v} for k, v in IT_LEVEL_CHOICES]


class ForeignLanguageLevel:
    LV1 = 1
    LV2 = 2
    LV3 = 3
    LV4 = 4
    LV5 = 5
    LV6 = 6


FOREIGN_LANGUAGE_LEVEL_CHOICES = (
    (ForeignLanguageLevel.LV1, "Bậc 1"),
    (ForeignLanguageLevel.LV2, "Bậc 2"),
    (ForeignLanguageLevel.LV3, "Bậc 3"),
    (ForeignLanguageLevel.LV4, "Bậc 4"),
    (ForeignLanguageLevel.LV5, "Bậc 5"),
    (ForeignLanguageLevel.LV6, "Bậc 6"),
)

FOREIGN_LANGUAGE_LEVEL_DIC = dict(FOREIGN_LANGUAGE_LEVEL_CHOICES)

FOREIGN_LANGUAGE_LEVELS = [
    {"value": k, "label": v} for k, v in FOREIGN_LANGUAGE_LEVEL_CHOICES
]


class PoliticalTheoryLevel:
    SC = 1
    TC = 2
    CC = 3
    CN = 4
    NONE = 5


POLITICAL_THEORY_LEVEL_CHOICES = (
    (PoliticalTheoryLevel.SC, "Sơ cấp"),
    (PoliticalTheoryLevel.TC, "Trung cấp"),
    (PoliticalTheoryLevel.CC, "Cao cấp"),
    (PoliticalTheoryLevel.CN, "Cử nhân"),
    (PoliticalTheoryLevel.NONE, "Chưa có"),
)

POLITICAL_THEORY_LEVEL_DIC = dict(POLITICAL_THEORY_LEVEL_CHOICES)

POLITICAL_THEORY_LEVELS = [
    {"value": k, "label": v} for k, v in POLITICAL_THEORY_LEVEL_CHOICES
]


class Gender:
    FEMALE = 0
    MALE = 1


GENDER_CHOICES = (
    (Gender.FEMALE, "Nữ"),
    (Gender.MALE, "Nam"),
)

GENDER_DICT = dict(GENDER_CHOICES)

GENDERS = [{"value": k, "label": v} for k, v in GENDER_CHOICES]
