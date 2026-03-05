import re

with open('landing_page.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Novo HTML da seção
new_section = """
    <!-- Video Section -->
    <section class="py-24 px-6 md:px-12 bg-background-dark text-white relative overflow-hidden flex flex-col items-center" id="video-tour" data-aos="fade-up">
        <div class="absolute inset-0 z-0 opacity-10">
            <div class="w-full h-full bg-cover bg-center" style="background-image: url('pilates_classico.png');"></div>
            <div class="absolute inset-0 bg-gradient-to-t from-background-dark via-background-dark/80 to-background-dark"></div>
        </div>
        
        <div class="relative z-10 w-full max-w-7xl mx-auto flex flex-col lg:flex-row items-center justify-center gap-16">
            <div class="lg:w-1/2 flex flex-col justify-center text-center lg:text-left">
                <span class="text-primary font-medium tracking-widest text-sm uppercase block mb-4 flex items-center justify-center lg:justify-start gap-2">
                    <span class="material-symbols-outlined text-lg">play_circle</span>
                    Assista ao Movimento
                </span>
                <h2 class="text-5xl md:text-6xl font-display font-medium mb-6 leading-tight">Inspiração e<br><span class="text-primary italic">Fluidez</span></h2>
                <p class="text-white/70 text-lg md:text-xl font-light mb-8 max-w-lg mx-auto lg:mx-0">
                    Sinta a atmosfera do nosso estúdio de perto. Cada movimento é conectado com a respiração para promover equilíbrio físico e mental em um ambiente de alto padrão.
                </p>
                <div class="flex justify-center lg:justify-start">
                    <a href="https://instagram.com/rhaisalinharespilates" target="_blank" class="glass-button text-white px-8 py-3 rounded-full text-base font-medium flex items-center gap-3 w-max">
                        <span class="material-symbols-outlined text-lg">photo_camera</span>
                        Mais no Instagram
                    </a>
                </div>
            </div>
            
            <div class="lg:w-1/2 flex justify-center lg:justify-end w-full">
                <!-- Wrapper for exactly 9:16 aspect ratio -->
                <div class="relative w-full max-w-[350px] aspect-[9/16] rounded-3xl overflow-hidden shadow-[0_20px_50px_rgba(0,0,0,0.5)] border border-white/10 group bg-neutral-dark/50">
                    <blockquote class="instagram-media absolute inset-0 w-full h-full m-0 p-0" data-instgrm-permalink="https://www.instagram.com/reel/DU8m2gJkfrW/?utm_source=ig_embed&amp;utm_campaign=loading" data-instgrm-version="14" style=" background:#FFF; border:0; border-radius:3px; margin: 1px; max-width:540px; min-width:326px; padding:0; width:99.375%; width:-webkit-calc(100% - 2px); width:calc(100% - 2px);">
                    </blockquote>
                </div>
            </div>
        </div>
    </section>
"""

# Embeds script needed for IG
ig_script = '<script async src="//www.instagram.com/embed.js"></script>'
if ig_script not in html:
    html = html.replace('</body>', f'    {ig_script}\n</body>')

# Regex to match the old Video Section
pattern = re.compile(r'<!-- Video Section -->.*?</section>', re.DOTALL)
html = pattern.sub(new_section.strip(), html)

with open('landing_page.html', 'w', encoding='utf-8') as f:
    f.write(html)
