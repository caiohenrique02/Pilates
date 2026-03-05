import re

with open('landing_page.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Novo estilo da div do iPhone:
# 1. Trocar o fundo do exterior (borda) para uma cor prateada/titânio.
# 2. Aumentar o max-w do container para ele ficar um pouco maior.
# 3. Adicionar uma borda interna discreta.
# 4. Modificar as cores da "Ilha Dinâmica" e dos botões para casar com a nova cor.

old_wrapper = r'                <!-- iPhone Mockup Frame -->\n                <div class="relative w-full max-w-\[320px\] aspect-\[9/16\] bg-black rounded-\[3rem\] shadow-\[0_20px_50px_rgba\(0,0,0,0\.7\)\] border-\[12px\] border-neutral-900 group">\n                    \n                    <!-- Dynamic Island Notch -->\n                    <div class="absolute top-0 inset-x-0 h-7 flex justify-center z-50">\n                        <div class="w-24 h-6 bg-black rounded-b-xl mt-\[-2px\] relative z-20"></div>\n                    </div>\n                    \n                    <!-- Buttons \(Left\) -->\n                    <div class="absolute -left-\[14px\] top-24 w-1 h-8 bg-neutral-800 rounded-l-md"></div>\n                    <div class="absolute -left-\[14px\] top-36 w-1 h-12 bg-neutral-800 rounded-l-md"></div>\n                    <div class="absolute -left-\[14px\] top-52 w-1 h-12 bg-neutral-800 rounded-l-md"></div>\n                    \n                    <!-- Button \(Right\) -->\n                    <div class="absolute -right-\[14px\] top-36 w-1 h-16 bg-neutral-800 rounded-r-md"></div>\n                    \n                    <!-- Screen/Iframe Container -->\n                    <div class="absolute inset-0 w-full h-full bg-black rounded-\[2rem\] overflow-hidden flex items-center justify-center pt-2">'

new_iphone_mockup = """
                <!-- iPhone Mockup Frame -->
                <div class="relative w-full max-w-[360px] aspect-[9/16] bg-neutral-200 rounded-[3.5rem] shadow-[0_25px_60px_rgba(255,255,255,0.1)] border-[14px] border-neutral-300 group">
                    
                    <!-- Dynamic Island Notch -->
                    <div class="absolute top-0 inset-x-0 h-7 flex justify-center z-50">
                        <div class="w-28 h-7 bg-neutral-900 rounded-b-2xl mt-[-2px] relative z-20 flex items-center justify-end px-3">
                            <div class="w-2 h-2 rounded-full bg-blue-900/50 mr-1"></div>
                            <div class="w-2 h-2 rounded-full bg-white/10"></div>
                        </div>
                    </div>
                    
                    <!-- Buttons (Left) -->
                    <div class="absolute -left-[16px] top-28 w-[2px] h-8 bg-neutral-400 rounded-l-md"></div>
                    <div class="absolute -left-[16px] top-40 w-[2px] h-14 bg-neutral-400 rounded-l-md"></div>
                    <div class="absolute -left-[16px] top-60 w-[2px] h-14 bg-neutral-400 rounded-l-md"></div>
                    
                    <!-- Button (Right) -->
                    <div class="absolute -right-[16px] top-40 w-[2px] h-20 bg-neutral-400 rounded-r-md"></div>
                    
                    <!-- Inner Bezel & Screen/Iframe Container -->
                    <div class="absolute inset-0 w-full h-full bg-black rounded-[2.8rem] overflow-hidden flex items-center justify-center p-[4px]">
                        <div class="w-full h-full rounded-[2.5rem] overflow-hidden bg-black flex items-center justify-center">
"""

html = re.sub(old_wrapper, new_iphone_mockup.strip(), html)

# Corrigir fechamento devido à div extra (Inner Bezel)

closing_tags = r'                    </blockquote>\n                    </div>\n                </div>'
new_closing_tags = '                    </blockquote>\n                        </div>\n                    </div>\n                </div>'
html = html.replace(closing_tags, new_closing_tags)

with open('landing_page.html', 'w', encoding='utf-8') as f:
    f.write(html)
