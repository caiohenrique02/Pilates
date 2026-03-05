import re

with open('landing_page.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Novo estilo da div que contém o iframe adicionando a moldura do iPhone (mockup via CSS puro e Tailwind)
# Vamos substituir a div: <div class="relative w-full max-w-[350px] aspect-[9/16] rounded-3xl overflow-hidden shadow-[0_20px_50px_rgba(0,0,0,0.5)] border border-white/10 group bg-neutral-dark/50">

old_wrapper = r'<div class="relative w-full max-w-\[350px\] aspect-\[9/16\] rounded-3xl overflow-hidden shadow-\[0_20px_50px_rgba\(0,0,0,0\.5\)\] border border-white/10 group bg-neutral-dark/50">'

iphone_mockup = """
                <!-- iPhone Mockup Frame -->
                <div class="relative w-full max-w-[320px] aspect-[9/16] bg-black rounded-[3rem] shadow-[0_20px_50px_rgba(0,0,0,0.7)] border-[12px] border-neutral-900 group">
                    
                    <!-- Dynamic Island Notch -->
                    <div class="absolute top-0 inset-x-0 h-7 flex justify-center z-50">
                        <div class="w-24 h-6 bg-black rounded-b-xl mt-[-2px] relative z-20"></div>
                    </div>
                    
                    <!-- Buttons (Left) -->
                    <div class="absolute -left-[14px] top-24 w-1 h-8 bg-neutral-800 rounded-l-md"></div>
                    <div class="absolute -left-[14px] top-36 w-1 h-12 bg-neutral-800 rounded-l-md"></div>
                    <div class="absolute -left-[14px] top-52 w-1 h-12 bg-neutral-800 rounded-l-md"></div>
                    
                    <!-- Button (Right) -->
                    <div class="absolute -right-[14px] top-36 w-1 h-16 bg-neutral-800 rounded-r-md"></div>
                    
                    <!-- Screen/Iframe Container -->
                    <div class="absolute inset-0 w-full h-full bg-black rounded-[2rem] overflow-hidden flex items-center justify-center pt-2">
"""

html = re.sub(old_wrapper, iphone_mockup.strip(), html)

# Fechar mais uma div, já que o mockup cria um container extra e um padding
# O iframe original é englobado por blockquote, e logo depois tem a </div> raiz
# A div antiga:
# <blockquote class="instagram-media ...> </blockquote> </div>
# Com o mockup temos:
# <div class="relative w-full ...">  <div class="absolute inset-x-0 ..."></div> <div class="absolute -left... => divs de botões ... <div class="absolute inset-0 ..."> blockquote... </div> </div>

closing_tags = r'                    </blockquote>\n                </div>'
new_closing_tags = '                    </blockquote>\n                    </div>\n                </div>'

html = html.replace(closing_tags, new_closing_tags)

with open('landing_page.html', 'w', encoding='utf-8') as f:
    f.write(html)
