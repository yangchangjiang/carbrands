#!/usr/bin/env python3
"""Build carbrands.world — 105 brands × 14 languages — RACING RED theme"""
import json, os, html

BASE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "carbrands.world"
LANGS = ["en","zh-CN","ja","ko","es","pt","fr","de","ar","hi","th","vi","id","ru"]
ACCENT = "#dc2626"  # Racing red

with open(os.path.join(BASE, "brands.json"),"r",encoding="utf-8") as f: brands = json.load(f)
with open(os.path.join(BASE, "cars.json"),"r",encoding="utf-8") as f: cars = json.load(f)

# Light theme with racing red accents
CSS = """:root{--bg:#fefefe;--surface:#f8f8f8;--surface2:#eee;--border:#ddd;--text:#18181b;--text2:#71717a;--accent:#dc2626;--accent2:#b91c1c;--accent-bg:#fef2f2;--radius:6px;--shadow:0 1px 2px rgba(0,0,0,.06)}*{box-sizing:border-box}body{font-family:system-ui;background:var(--bg);color:var(--text);line-height:1.6;margin:0}header{background:linear-gradient(135deg,#18181b,#27272a);color:white;padding:0}nav{max-width:1200px;margin:0 auto;display:flex;gap:20px;align-items:center;padding:14px 24px;flex-wrap:wrap}nav a{color:#d4d4d8;text-decoration:none;font-size:.9rem;font-weight:500;transition:color .2s}nav a:hover{color:white}.logo{font-size:1.4rem;font-weight:900;color:var(--accent);letter-spacing:-.5px}nav .logo{color:var(--accent)}.hero{background:linear-gradient(135deg,#18181b 0%,#27272a 50%,#dc2626 200%);color:white;padding:80px 24px;text-align:center;position:relative;overflow:hidden}.hero::after{content:'';position:absolute;bottom:0;left:0;right:0;height:4px;background:var(--accent)}.hero h1{font-size:2.8rem;font-weight:900;letter-spacing:-1px;margin:0}.hero p{font-size:1.2rem;opacity:.8;margin:12px 0 0}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:12px;max-width:1200px;margin:32px auto;padding:0 24px}.brand-card{background:white;border:1px solid var(--border);border-radius:var(--radius);padding:20px 16px;text-decoration:none;color:var(--text);transition:all .2s;text-align:center;box-shadow:var(--shadow)}.brand-card:hover{transform:translateY(-3px);box-shadow:0 4px 16px rgba(220,38,38,.15);border-color:var(--accent)}.brand-name{font-weight:700;font-size:1.05rem;margin:8px 0 4px}.brand-country{font-size:.8rem;color:var(--text2)}.brand-models{font-size:.75rem;color:var(--accent);font-weight:600;margin-top:4px}.detail-hero{background:linear-gradient(135deg,#18181b,#27272a);color:white;padding:60px 24px 80px;text-align:center;position:relative}.detail-hero .brand-name-lg{font-size:3rem;font-weight:900;letter-spacing:-1px}.detail-hero .brand-sub{font-size:1.1rem;opacity:.7;margin-top:8px}.model-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px;max-width:1200px;margin:-40px auto 40px;padding:0 24px;position:relative;z-index:1}.model-card{background:white;border:1px solid var(--border);border-radius:var(--radius);padding:24px;box-shadow:var(--shadow);transition:all .2s}.model-card:hover{transform:translateY(-2px);box-shadow:0 4px 20px rgba(0,0,0,.1)}.model-name{font-size:1.2rem;font-weight:700;color:var(--accent)}.model-specs{display:grid;grid-template-columns:1fr 1fr;gap:8px 20px;margin-top:12px;font-size:.85rem}.model-specs .spec-value{font-size:.85rem;word-break:break-word}.spec-label{color:var(--text2);font-size:.8rem}.spec-value{font-weight:600}.car-detail-hero{background:linear-gradient(135deg,#dc2626,#991b1b);color:white;padding:60px 24px 80px;text-align:center}.car-detail-hero .car-name{font-size:2.4rem;font-weight:900}.car-detail-hero .car-brand{font-size:1.1rem;opacity:.7;margin-top:8px}.car-specs-card{background:white;max-width:800px;margin:-40px auto 40px;border:1px solid var(--border);border-radius:var(--radius);padding:32px;box-shadow:var(--shadow);position:relative;z-index:1}.car-specs-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:16px}.car-spec{border:1px solid var(--border);border-radius:8px;padding:16px;text-align:center}.car-spec .sv{font-size:1.1rem;font-weight:800;color:var(--accent);word-break:break-word;overflow-wrap:break-word}.car-spec .sl{font-size:.7rem;color:var(--text2);margin-top:4px;text-transform:uppercase;letter-spacing:.5px}.car-spec{overflow:hidden}.lang-wrap{position:relative}.lang-btn{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);padding:8px 16px;border-radius:20px;cursor:pointer;font-size:.85rem;color:white}.lang-dropdown{display:none;position:absolute;top:100%;right:0;background:white;border:1px solid var(--border);border-radius:8px;box-shadow:0 4px 20px rgba(0,0,0,.2);z-index:201;min-width:160px;padding:8px 0;max-height:300px;overflow-y:auto}.lang-dropdown.show{display:block}.lang-dropdown button{display:block;width:100%;text-align:left;padding:8px 20px;border:none;background:none;font-size:.85rem;cursor:pointer;color:var(--text)}.lang-dropdown button:hover{background:var(--accent-bg)}.cookie-consent{position:fixed;bottom:0;left:0;right:0;background:#18181b;color:white;padding:16px 24px;z-index:9999;display:flex;justify-content:space-between;align-items:center;gap:12px;font-size:.85rem}.cookie-btns{display:flex;gap:8px}.cookie-accept{background:var(--accent);color:white;border:none;padding:8px 24px;border-radius:4px;cursor:pointer;font-weight:600}.cookie-decline{background:#3f3f46;color:white;border:none;padding:8px 24px;border-radius:4px;cursor:pointer}footer{background:#18181b;color:#a1a1aa;padding:40px 24px;text-align:center;font-size:.85rem;margin-top:80px}a{color:var(--accent);text-decoration:none}@media(max-width:600px){.hero h1{font-size:1.8rem}.grid{grid-template-columns:repeat(auto-fill,minmax(140px,1fr))}.detail-hero .brand-name-lg{font-size:2rem}}"""

DROPDOWN = '<div class="lang-wrap"><button class="lang-btn" onclick="this.nextElementSibling.classList.toggle(\'show\')">🌐</button><div class="lang-dropdown"><button onclick="goLang(\'en\')">English</button><button onclick="goLang(\'zh-CN\')">简体中文</button><button onclick="goLang(\'ja\')">日本語</button><button onclick="goLang(\'ko\')">한국어</button><button onclick="goLang(\'es\')">Español</button><button onclick="goLang(\'pt\')">Português</button><button onclick="goLang(\'fr\')">Français</button><button onclick="goLang(\'de\')">Deutsch</button><button onclick="goLang(\'ar\')">العربية</button><button onclick="goLang(\'hi\')">हिन्दी</button><button onclick="goLang(\'th\')">ไทย</button><button onclick="goLang(\'vi\')">Tiếng Việt</button><button onclick="goLang(\'id\')">Bahasa Indonesia</button><button onclick="goLang(\'ru\')">Русский</button></div></div>'

GOLANG = '<script>var LANGS=["en","zh-CN","ja","ko","es","pt","fr","de","ar","hi","th","vi","id","ru"];function goLang(l){var p=window.location.pathname;for(var i=0;i<LANGS.length;i++){if(p.indexOf("/"+LANGS[i]+"/")>=0){if(l==="en"){window.location.href=p.replace("/"+LANGS[i]+"/","/")}else{window.location.href=p.replace("/"+LANGS[i]+"/","/"+l+"/")}return}}var parts=p.split("/").filter(function(x){return x.length>0});var pg=parts.join("/")||"index.html";if(l==="en"){window.location.href="/"+pg}else{window.location.href="/"+l+"/"+pg}}document.addEventListener("click",function(e){if(!e.target.closest(".lang-wrap")){var d=document.querySelector(".lang-dropdown");if(d)d.classList.remove("show")}});</script>'

ADS = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4047761093600857" crossorigin="anonymous"></script>'
BAIDU = '<script>(function(){var bp=document.createElement("script");bp.src="//push.zhanzhang.baidu.com/push.js";var s=document.getElementsByTagName("script")[0];s.parentNode.insertBefore(bp,s);})();</script>'

UI = {
    "en":{"home":"Home","brands":"brands","models":"models","browse_all":"Browse all","founded":"Founded","types":"Types","country":"Country","description":"Description","popular_brands":"Popular Car Brands","view_brand":"View Brand","specs":"Specifications","horsepower":"HP","fuel":"Fuel","seats":"Seats","price":"Price","year":"Year","body":"Body Type"},
    "zh-CN":{"home":"首页","brands":"个品牌","models":"款车型","browse_all":"浏览全部","founded":"创立","types":"类型","country":"国家","description":"简介","popular_brands":"热门汽车品牌","view_brand":"查看品牌","specs":"规格","horsepower":"马力","fuel":"燃料","seats":"座位","price":"售价","year":"年份","body":"车身"},
    "ja":{"home":"ホーム","brands":"ブランド","models":"モデル","browse_all":"すべて","founded":"設立","types":"タイプ","country":"国","description":"説明","popular_brands":"人気ブランド","view_brand":"詳細","specs":"スペック","horsepower":"馬力","fuel":"燃料","seats":"座席","price":"価格","year":"年式","body":"ボディ"},
    "ko":{"home":"홈","brands":"브랜드","models":"모델","browse_all":"전체","founded":"설립","types":"유형","country":"국가","description":"설명","popular_brands":"인기 브랜드","view_brand":"보기","specs":"제원","horsepower":"마력","fuel":"연료","seats":"좌석","price":"가격","year":"연식","body":"차체"},
    "es":{"home":"Inicio","brands":"marcas","models":"modelos","browse_all":"Explorar","founded":"Fundado","types":"Tipos","country":"País","description":"Descripción","popular_brands":"Marcas Populares","view_brand":"Ver Marca","specs":"Especificaciones","horsepower":"CV","fuel":"Combustible","seats":"Asientos","price":"Precio","year":"Año","body":"Carrocería"},
    "pt":{"home":"Início","brands":"marcas","models":"modelos","browse_all":"Explorar","founded":"Fundado","types":"Tipos","country":"País","description":"Descrição","popular_brands":"Marcas Populares","view_brand":"Ver","specs":"Especificações","horsepower":"CV","fuel":"Combustível","seats":"Assentos","price":"Preço","year":"Ano","body":"Categoria"},
    "fr":{"home":"Accueil","brands":"marques","models":"modèles","browse_all":"Parcourir","founded":"Fondé","types":"Types","country":"Pays","description":"Description","popular_brands":"Marques Populaires","view_brand":"Voir","specs":"Spécifications","horsepower":"CV","fuel":"Carburant","seats":"Places","price":"Prix","year":"Année","body":"Carrosserie"},
    "de":{"home":"Start","brands":"Marken","models":"Modelle","browse_all":"Alle","founded":"Gegründet","types":"Typen","country":"Land","description":"Beschreibung","popular_brands":"Beliebte Marken","view_brand":"Details","specs":"Technische Daten","horsepower":"PS","fuel":"Kraftstoff","seats":"Sitze","price":"Preis","year":"Jahr","body":"Karosserie"},
    "ar":{"home":"الرئيسية","brands":"علامة","models":"موديل","browse_all":"تصفح","founded":"تأسست","types":"أنواع","country":"بلد","description":"وصف","popular_brands":"علامات مشهورة","view_brand":"تفاصيل","specs":"المواصفات","horsepower":"حصان","fuel":"الوقود","seats":"مقاعد","price":"السعر","year":"السنة","body":"نوع الهيكل"},
    "hi":{"home":"होम","brands":"ब्रांड","models":"मॉडल","browse_all":"सभी","founded":"स्थापित","types":"प्रकार","country":"देश","description":"विवरण","popular_brands":"लोकप्रिय ब्रांड","view_brand":"देखें","specs":"स्पेक्स","horsepower":"एचपी","fuel":"ईंधन","seats":"सीटें","price":"कीमत","year":"वर्ष","body":"बॉडी"},
    "th":{"home":"หน้าแรก","brands":"แบรนด์","models":"รุ่น","browse_all":"ทั้งหมด","founded":"ก่อตั้ง","types":"ประเภท","country":"ประเทศ","description":"คำอธิบาย","popular_brands":"แบรนด์ยอดนิยม","view_brand":"ดู","specs":"สเปก","horsepower":"แรงม้า","fuel":"เชื้อเพลิง","seats":"ที่นั่ง","price":"ราคา","year":"ปี","body":"ตัวถัง"},
    "vi":{"home":"Trang chủ","brands":"thương hiệu","models":"mẫu xe","browse_all":"Tất cả","founded":"Thành lập","types":"Loại","country":"Quốc gia","description":"Mô tả","popular_brands":"Thương Hiệu Phổ Biến","view_brand":"Xem","specs":"Thông số","horsepower":"Mã lực","fuel":"Nhiên liệu","seats":"Chỗ","price":"Giá","year":"Năm","body":"Kiểu"},
    "id":{"home":"Beranda","brands":"merek","models":"model","browse_all":"Semua","founded":"Didirikan","types":"Tipe","country":"Negara","description":"Deskripsi","popular_brands":"Merek Populer","view_brand":"Lihat","specs":"Spesifikasi","horsepower":"HP","fuel":"Bahan Bakar","seats":"Kursi","price":"Harga","year":"Tahun","body":"Tipe"},
    "ru":{"home":"Главная","brands":"брендов","models":"моделей","browse_all":"Все","founded":"Основан","types":"Типы","country":"Страна","description":"Описание","popular_brands":"Популярные Бренды","view_brand":"Подробнее","specs":"Характеристики","horsepower":"Л.С.","fuel":"Топливо","seats":"Мест","price":"Цена","year":"Год","body":"Кузов"},
}

COOKIE = {"en":("We use cookies for ads.","Accept","Decline"),"zh-CN":("本站使用Cookie用于广告。","接受","拒绝"),"ja":("広告にCookieを使用します。","許可","拒否"),"ko":("광고용 쿠키 사용.","수락","거절"),"es":("Usamos cookies para anuncios.","Aceptar","Rechazar"),"pt":("Usamos cookies para anúncios.","Aceitar","Recusar"),"fr":("Nous utilisons des cookies.","Accepter","Refuser"),"de":("Wir nutzen Cookies für Werbung.","Akzeptieren","Ablehnen"),"ar":("نستخدم ملفات الارتباط للإعلانات.","موافق","رفض"),"hi":("विज्ञापन के लिए कुकीज़.","स्वीकार","अस्वीकार"),"th":("ใช้คุกกี้เพื่อโฆษณา","ยอมรับ","ปฏิเสธ"),"vi":("Chúng tôi dùng cookie cho quảng cáo.","Chấp nhận","Từ chối"),"id":("Kami menggunakan cookie untuk iklan.","Terima","Tolak"),"ru":("Используем куки для рекламы.","Принять","Отклонить")}

COUNTRY_TR = {
    "zh-CN":{"Japan":"日本","Germany":"德国","United States":"美国","South Korea":"韩国","China":"中国","France":"法国","Italy":"意大利","Sweden":"瑞典","United Kingdom":"英国","India":"印度","Malaysia":"马来西亚","Spain":"西班牙","Czech Republic":"捷克","Romania":"罗马尼亚","Russia":"俄罗斯","Vietnam":"越南"},
    "ja":{"Japan":"日本","Germany":"ドイツ","United States":"アメリカ","South Korea":"韓国","China":"中国","France":"フランス","Italy":"イタリア","Sweden":"スウェーデン","United Kingdom":"イギリス","India":"インド","Russia":"ロシア","Vietnam":"ベトナム"},
    "ko":{"Japan":"일본","Germany":"독일","United States":"미국","South Korea":"한국","China":"중국","France":"프랑스","Italy":"이탈리아","Sweden":"스웨덴","United Kingdom":"영국","India":"인도","Russia":"러시아"},
}



# SVG car illustrations by body type
CAR_SVGS = {
    "Sedan": '<svg viewBox="0 0 300 140" style="width:300px;height:140px"><path d="M30 100 L40 75 L260 75 L270 100 L280 100 L280 115 L20 115 L20 100 Z" fill="#dc2626"/><rect x="60" y="60" width="80" height="20" rx="10" fill="#b91c1c"/><rect x="150" y="60" width="80" height="20" rx="10" fill="#b91c1c"/><circle cx="90" cy="118" r="16" fill="#27272a"/><circle cx="90" cy="118" r="8" fill="#52525b"/><circle cx="220" cy="118" r="16" fill="#27272a"/><circle cx="220" cy="118" r="8" fill="#52525b"/></svg>',
    "SUV": '<svg viewBox="0 0 300 140" style="width:300px;height:140px"><path d="M20 85 L25 60 L255 60 L280 85 L290 85 L290 115 L10 115 Z" fill="#dc2626"/><rect x="50" y="42" width="60" height="22" rx="8" fill="#b91c1c"/><rect x="120" y="42" width="60" height="22" rx="8" fill="#b91c1c"/><rect x="190" y="42" width="60" height="22" rx="8" fill="#b91c1c"/><circle cx="80" cy="118" r="18" fill="#27272a"/><circle cx="80" cy="118" r="9" fill="#52525b"/><circle cx="230" cy="118" r="18" fill="#27272a"/><circle cx="230" cy="118" r="9" fill="#52525b"/></svg>',
    "Coupe": '<svg viewBox="0 0 300 140" style="width:300px;height:140px"><path d="M40 100 L70 80 L120 65 L230 65 L250 80 L270 100 L280 100 L280 115 L20 115 L20 100 Z" fill="#dc2626"/><rect x="80" y="52" width="50" height="16" rx="6" fill="#18181b"/><rect x="140" y="52" width="50" height="16" rx="6" fill="#18181b"/><circle cx="90" cy="118" r="16" fill="#27272a"/><circle cx="90" cy="118" r="8" fill="#52525b"/><circle cx="220" cy="118" r="16" fill="#27272a"/><circle cx="220" cy="118" r="8" fill="#52525b"/></svg>',
    "Truck": '<svg viewBox="0 0 300 140" style="width:300px;height:140px"><path d="M10 85 L15 55 L100 55 L100 85 L280 85 L290 85 L290 115 L10 115 Z" fill="#dc2626"/><rect x="25" y="35" width="60" height="24" rx="8" fill="#b91c1c"/><rect x="110" y="65" width="170" height="25" rx="4" fill="#991b1b"/><circle cx="60" cy="118" r="17" fill="#27272a"/><circle cx="60" cy="118" r="8" fill="#52525b"/><circle cx="240" cy="118" r="17" fill="#27272a"/><circle cx="240" cy="118" r="8" fill="#52525b"/></svg>',
    "Hatchback": '<svg viewBox="0 0 300 140" style="width:300px;height:140px"><path d="M25 100 L35 75 L250 75 L280 90 L280 100 L290 100 L290 115 L10 115 L10 100 Z" fill="#dc2626"/><rect x="55" y="58" width="70" height="22" rx="10" fill="#b91c1c"/><rect x="135" y="58" width="70" height="22" rx="10" fill="#b91c1c"/><circle cx="80" cy="118" r="15" fill="#27272a"/><circle cx="80" cy="118" r="7" fill="#52525b"/><circle cx="220" cy="118" r="15" fill="#27272a"/><circle cx="220" cy="118" r="7" fill="#52525b"/></svg>',
    "Convertible": '<svg viewBox="0 0 300 140" style="width:300px;height:140px"><path d="M40 100 L70 85 L230 85 L260 100 L280 100 L280 115 L20 115 L20 100 Z" fill="#dc2626"/><rect x="80" y="72" width="60" height="10" rx="3" fill="#18181b"/><rect x="150" y="72" width="60" height="10" rx="3" fill="#18181b"/><circle cx="90" cy="118" r="16" fill="#27272a"/><circle cx="90" cy="118" r="8" fill="#52525b"/><circle cx="220" cy="118" r="16" fill="#27272a"/><circle cx="220" cy="118" r="8" fill="#52525b"/></svg>',
    "Wagon": '<svg viewBox="0 0 300 140" style="width:300px;height:140px"><path d="M20 90 L25 60 L260 60 L280 90 L290 90 L290 115 L10 115 Z" fill="#dc2626"/><rect x="50" y="44" width="70" height="20" rx="8" fill="#b91c1c"/><rect x="130" y="44" width="70" height="20" rx="8" fill="#b91c1c"/><circle cx="80" cy="118" r="15" fill="#27272a"/><circle cx="80" cy="118" r="7" fill="#52525b"/><circle cx="220" cy="118" r="15" fill="#27272a"/><circle cx="220" cy="118" r="7" fill="#52525b"/></svg>',
    "Minivan": '<svg viewBox="0 0 300 140" style="width:300px;height:140px"><path d="M15 80 L20 45 L270 45 L280 80 L290 80 L290 115 L10 115 Z" fill="#dc2626"/><rect x="45" y="28" width="65" height="22" rx="8" fill="#b91c1c"/><rect x="120" y="28" width="65" height="22" rx="8" fill="#b91c1c"/><rect x="195" y="28" width="65" height="22" rx="8" fill="#b91c1c"/><circle cx="80" cy="118" r="17" fill="#27272a"/><circle cx="80" cy="118" r="8" fill="#52525b"/><circle cx="230" cy="118" r="17" fill="#27272a"/><circle cx="230" cy="118" r="8" fill="#52525b"/></svg>',
}

def build_car_page(c, lang):
    ui, lp, cookie = UI.get(lang,UI["en"]), "" if lang=="en" else lang+"/", COOKIE.get(lang,COOKIE["en"])
    b = next((x for x in brands if x["id"]==c["brand_id"]), None)
    loc = COUNTRY_TR.get(lang,{}).get(b["country"],b["country"]) if b else c["brand"]
    car_svg = CAR_SVGS.get(c["body"], CAR_SVGS["Sedan"])
    brand_slug = c["brand_slug"]
    model_name = html.escape(c["model"])
    hreflang = "\n".join([f'<link rel="alternate" hreflang="{l}" href="https://{DOMAIN}/{("" if l=="en" else l+"/")}car/{brand_slug}/{c["model"].lower().replace(" ","-")}">' for l in LANGS])
    bc = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://{DOMAIN}/{lp}"}},{{"@type":"ListItem","position":2,"name":"{c["brand"]}","item":"https://{DOMAIN}/{lp}brand/{brand_slug}"}},{{"@type":"ListItem","position":3,"name":"{c["model"]}"}}]}}</script>'
    return f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{c["model"]} — {c["brand"]} {ui["specs"]} | {DOMAIN}</title><meta name="description" content="{c["model"]} {ui["specs"]}. {c["brand"]} - {ui["horsepower"]}: {c["horsepower"]}, {ui["fuel"]}: {c["fuel"]}, {ui["seats"]}: {c["seats"]}, {ui["price"]}: {c["price"]}. {ui["country"]}: {loc}."><meta name="keywords" content="{c["model"]}, {c["model"]} specs, {c["model"]} horsepower, {c["model"]} price, {c["brand"]} {c["model"]}"><style>{CSS}</style>{ADS}{hreflang}</head><body><header><nav><span class="logo">🏎️ {DOMAIN}</span><a href="/{lp}">{ui["home"]}</a><a href="/{lp}brand/{brand_slug}">{c["brand"]}</a>{DROPDOWN}</nav></header><div class="car-detail-hero"><div style="margin-bottom:12px">{car_svg}</div><div class="car-name">{model_name}</div><div class="car-brand">{c["brand"]} · {c["body"]}</div></div><div class="car-specs-card"><div class="car-specs-grid"><div class="car-spec"><div class="sv">{c["horsepower"]}</div><div class="sl">{ui["horsepower"]}</div></div><div class="car-spec"><div class="sv">{c["fuel"]}</div><div class="sl">{ui["fuel"]}</div></div><div class="car-spec"><div class="sv">{c["seats"]}</div><div class="sl">{ui["seats"]}</div></div><div class="car-spec"><div class="sv">{c["price"]}</div><div class="sl">{ui["price"]}</div></div><div class="car-spec"><div class="sv">{c["year"]}</div><div class="sl">{ui["year"]}</div></div><div class="car-spec"><div class="sv">{c["body"]}</div><div class="sl">{ui["body"]}</div></div></div></div><footer>&copy; 2026 {DOMAIN}</footer><div class="cookie-consent"><span>{cookie[0]}</span><div class="cookie-btns"><button class="cookie-accent" onclick="this.parentElement.parentElement.style.display=\'none\'" style="background:var(--accent);color:white;border:none;padding:8px 24px;border-radius:4px;cursor:pointer;font-weight:600">{cookie[1]}</button><button class="cookie-decline" onclick="this.parentElement.parentElement.style.display=\'none\'" style="background:#3f3f46;color:white;border:none;padding:8px 24px;border-radius:4px;cursor:pointer">{cookie[2]}</button></div></div>{GOLANG}{BAIDU}{bc}</body></html>'


# Fuel type translations
FUEL_TR = {
    "zh-CN": {"Gasoline":"汽油","Hybrid":"混动","Electric":"电动","Gasoline/Hybrid":"汽油/混动","Gasoline/Electric":"汽油/电动","Electric/Hybrid":"电动/混动"},
    "ja": {"Gasoline":"ガソリン","Hybrid":"ハイブリッド","Electric":"電気","Gasoline/Hybrid":"ガソリン/HV"},
    "ko": {"Gasoline":"가솔린","Hybrid":"하이브리드","Electric":"전기"},
    "es": {"Gasoline":"Gasolina","Hybrid":"Híbrido","Electric":"Eléctrico"},
    "pt": {"Gasoline":"Gasolina","Hybrid":"Híbrido","Electric":"Elétrico"},
    "fr": {"Gasoline":"Essence","Hybrid":"Hybride","Electric":"Électrique"},
    "de": {"Gasoline":"Benzin","Hybrid":"Hybrid","Electric":"Elektro"},
    "ar": {"Gasoline":"بنزين","Hybrid":"هايبرد","Electric":"كهرباء"},
    "ru": {"Gasoline":"Бензин","Hybrid":"Гибрид","Electric":"Электро"},
}

def build_index(lang):
    ui, lp, cookie = UI.get(lang,UI["en"]), "" if lang=="en" else lang+"/", COOKIE.get(lang,COOKIE["en"])
    cards = ""
    for b in brands[:60]:
        loc = COUNTRY_TR.get(lang,{}).get(b["country"],b["country"])
        cards += f'<a class="brand-card" href="/{lp}brand/{b["slug"]}"><span style="font-size:2rem">🚗</span><div class="brand-name">{html.escape(b["name"])}</div><div class="brand-country">{loc}</div><div class="brand-models">{b["model_count"]} {ui["models"]}</div></a>\n'
    hreflang = "\n".join([f'<link rel="alternate" hreflang="{l}" href="https://{DOMAIN}/{("" if l=="en" else l+"/")}">' for l in LANGS])
    faq = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"How many car brands?","acceptedAnswer":{{"@type":"Answer","text":"{len(brands)} car brands with models, specs and pricing."}}}}]}}</script>'
    return f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{ui["popular_brands"]} — {len(brands)} {ui["brands"]} | {DOMAIN}</title><meta name="description" content="{ui["browse_all"]} {len(brands)} {ui["brands"]}. {len(cars)} {ui["models"]}. {ui["specs"]}: horsepower, fuel, seats, price."><meta name="keywords" content="car brands, model specs, car horsepower, car fuel type, auto brands"><style>{CSS}</style>{ADS}{hreflang}</head><body><header><nav><span class="logo">🏎️ {DOMAIN}</span><a href="/{lp}">{ui["home"]}</a>{DROPDOWN}</nav></header><div class="hero"><h1>{ui["popular_brands"]}</h1><p>{ui["browse_all"]} {len(brands)} {ui["brands"]}, {len(cars)} {ui["models"]}</p></div><div class="grid">{cards}</div><footer>&copy; 2026 {DOMAIN}</footer><div class="cookie-consent"><span>{cookie[0]}</span><div class="cookie-btns"><button class="cookie-accept" onclick="this.parentElement.parentElement.style.display=\'none\'">{cookie[1]}</button><button class="cookie-decline" onclick="this.parentElement.parentElement.style.display=\'none\'">{cookie[2]}</button></div></div>{GOLANG}{BAIDU}{faq}</body></html>'

def build_brand_page(b, lang):
    ui, lp, cookie = UI.get(lang,UI["en"]), "" if lang=="en" else lang+"/", COOKIE.get(lang,COOKIE["en"])
    b_cars = [c for c in cars if c["brand_id"]==b["id"]]
    loc = COUNTRY_TR.get(lang,{}).get(b["country"],b["country"])
    model_cards = ""
    for c in b_cars:
        model_cards += f'<a href="/{lp}car/{c["brand_slug"]}/{c["model"].lower().replace(" ","-")}.html" class="model-card" style="text-decoration:none;color:inherit"><div class="model-name">{html.escape(c["model"])}</div><div class="model-specs"><div><span class="spec-label">{ui["horsepower"]}</span><br><span class="spec-value">{c["horsepower"]}</span></div><div><span class="spec-label">{ui["fuel"]}</span><br><span class="spec-value">{FUEL_TR.get(lang,{}).get(c["fuel"],c["fuel"])}</span></div><div><span class="spec-label">{ui["seats"]}</span><br><span class="spec-value">{c["seats"]}</span></div><div><span class="spec-label">{ui["price"]}</span><br><span class="spec-value">{c["price"]}</span></div></div></a>\n'
    hreflang = "\n".join([f'<link rel="alternate" hreflang="{l}" href="https://{DOMAIN}/{("" if l=="en" else l+"/")}brand/{b["slug"]}">' for l in LANGS])
    faq = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"What cars does {b["name"]} make?","acceptedAnswer":{{"@type":"Answer","text":"{b["name"]} makes {len(b_cars)} models including {", ".join(c["model"] for c in b_cars[:3])}."}}}}]}}</script>'
    bc = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://{DOMAIN}/{lp}"}},{{"@type":"ListItem","position":2,"name":"{b["name"]}"}}]}}</script>'
    return f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{b["name"]} — {len(b_cars)} {ui["models"]} | {DOMAIN}</title><meta name="description" content="{b["name"]} {ui["brands"]}. {ui["founded"]}: {b["founded"]}. {ui["country"]}: {loc}. {len(b_cars)} {ui["models"]}. {b["description"]}"><meta name="keywords" content="{b["name"]}, {b["name"]} models, {b["name"]} specs, {b["name"]} cars"><style>{CSS}</style>{ADS}{hreflang}</head><body><header><nav><span class="logo">🏎️ {DOMAIN}</span><a href="/{lp}">{ui["home"]}</a>{DROPDOWN}</nav></header><div class="detail-hero"><div class="brand-name-lg">{html.escape(b["name"])}</div><div class="brand-sub">{loc} · {ui["founded"]} {b["founded"]} · {len(b_cars)} {ui["models"]}</div></div><div class="model-grid">{model_cards}</div><footer>&copy; 2026 {DOMAIN}</footer><div class="cookie-consent"><span>{cookie[0]}</span><div class="cookie-btns"><button class="cookie-accent" onclick="this.parentElement.parentElement.style.display=\'none\'" style="background:var(--accent);color:white;border:none;padding:8px 24px;border-radius:4px;cursor:pointer;font-weight:600">{cookie[1]}</button><button class="cookie-decline" onclick="this.parentElement.parentElement.style.display=\'none\'" style="background:#3f3f46;color:white;border:none;padding:8px 24px;border-radius:4px;cursor:pointer">{cookie[2]}</button></div></div>{GOLANG}{BAIDU}{faq}{bc}</body></html>'

# Build
total = 0
for lang in LANGS:
    d = BASE if lang=="en" else os.path.join(BASE,lang)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d,"index.html"),"w",encoding="utf-8") as f: f.write(build_index(lang)); total += 1
    bd = os.path.join(d,"brand"); os.makedirs(bd, exist_ok=True)
    for b in brands:
        with open(os.path.join(bd, b["slug"]+".html"),"w",encoding="utf-8") as f: f.write(build_brand_page(b,lang)); total += 1
    print(f"  ✓ {lang}: {1+len(brands)} pages")

# Generate car model pages
for lang in LANGS:
    d = BASE if lang=="en" else os.path.join(BASE,lang)
    cd_dir = os.path.join(d,"car")
    for c in cars:
        c_dir = os.path.join(cd_dir, c["brand_slug"])
        os.makedirs(c_dir, exist_ok=True)
        slug = c["model"].lower().replace(" ","-")
        with open(os.path.join(c_dir, slug+".html"),"w",encoding="utf-8") as f:
            f.write(build_car_page(c,lang))
        total += 1
    print(f"  🚗 cars {lang}: {len(cars)} pages")

# ads.txt + privacy + sitemap
with open(os.path.join(BASE,"ads.txt"),"w") as f: f.write("google.com, pub-4047761093600857, DIRECT, f08c47fec0942fa0")
for lang in LANGS:
    d = BASE if lang=="en" else os.path.join(BASE,lang)
    with open(os.path.join(d,"privacy.html"),"w",encoding="utf-8") as f: f.write(f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="UTF-8"><title>Privacy | {DOMAIN}</title></head><body style="font-family:system-ui;max-width:800px;margin:0 auto;padding:20px"><h1>Privacy Policy</h1><p>This site uses Google AdSense. Contact: admin@{DOMAIN}</p></body></html>')

urls = [f"https://{DOMAIN}/"]
for lang in LANGS:
    lp = "" if lang=="en" else lang+"/"
    urls.append(f"https://{DOMAIN}/{lp}")
    for b in brands:
        urls.append(f"https://{DOMAIN}/{lp}brand/{b['slug']}")
    for c in cars:
        c_slug = c["model"].lower().replace(" ","-")
        urls.append(f"https://{DOMAIN}/{lp}car/{c['brand_slug']}/{c_slug}")
with open(os.path.join(BASE,"sitemap.xml"),"w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    for u in sorted(set(urls)): f.write(f"  <url><loc>{u}</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>\n")
    f.write('</urlset>')

print(f"\n✓ Total: {total} HTML pages + sitemap ({len(set(urls))} URLs)")
