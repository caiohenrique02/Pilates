import re

with open('landing_page.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replacement 1: The services section
new_services_html = """        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 px-4 md:max-w-7xl md:mx-auto pb-12">
            <!-- Service 1 -->
            <div onclick="openServiceModal('classico')" class="group relative h-[450px] w-full overflow-hidden rounded-3xl shadow-xl cursor-pointer transform hover:-translate-y-2 transition-all duration-500">
                <div class="absolute inset-0">
                    <div class="w-full h-full bg-cover bg-center transition-transform duration-1000 group-hover:scale-110" style="background-image: url('pilates_classico.png');"></div>
                    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent opacity-80 group-hover:opacity-100 transition-opacity duration-500"></div>
                </div>
                <div class="absolute bottom-0 left-0 p-8 w-full z-10 text-white translate-y-4 group-hover:translate-y-0 transition-transform duration-500">
                    <div class="w-12 h-12 rounded-full bg-white/10 backdrop-blur-md flex items-center justify-center mb-6 border border-white/20">
                        <span class="material-symbols-outlined text-2xl text-primary">self_improvement</span>
                    </div>
                    <h3 class="text-3xl font-display mb-2">Pilates Clássico</h3>
                    <p class="text-sm text-white/80 opacity-0 group-hover:opacity-100 transition-opacity duration-500 delay-100 flex items-center gap-2">
                        Ver detalhes <span class="material-symbols-outlined text-sm">arrow_forward</span>
                    </p>
                </div>
            </div>

            <!-- Service 2 -->
            <div onclick="openServiceModal('gestantes')" class="group relative h-[450px] w-full overflow-hidden rounded-3xl shadow-xl cursor-pointer transform hover:-translate-y-2 transition-all duration-500">
                <div class="absolute inset-0">
                    <div class="w-full h-full bg-cover bg-center transition-transform duration-1000 group-hover:scale-110" style="background-image: url('pilates_gestantes.png');"></div>
                    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent opacity-80 group-hover:opacity-100 transition-opacity duration-500"></div>
                </div>
                <div class="absolute bottom-0 left-0 p-8 w-full z-10 text-white translate-y-4 group-hover:translate-y-0 transition-transform duration-500">
                    <div class="w-12 h-12 rounded-full bg-white/10 backdrop-blur-md flex items-center justify-center mb-6 border border-white/20">
                        <span class="material-symbols-outlined text-2xl text-primary">pregnant_woman</span>
                    </div>
                    <h3 class="text-3xl font-display mb-2">Gestantes</h3>
                    <p class="text-sm text-white/80 opacity-0 group-hover:opacity-100 transition-opacity duration-500 delay-100 flex items-center gap-2">
                        Ver detalhes <span class="material-symbols-outlined text-sm">arrow_forward</span>
                    </p>
                </div>
            </div>

            <!-- Service 3 -->
            <div onclick="openServiceModal('reabilitacao')" class="group relative h-[450px] w-full overflow-hidden rounded-3xl shadow-xl cursor-pointer transform hover:-translate-y-2 transition-all duration-500">
                <div class="absolute inset-0">
                    <div class="w-full h-full bg-cover bg-center transition-transform duration-1000 group-hover:scale-110" style="background-image: url('pilates_reabilitacao.png');"></div>
                    <div class="absolute inset-0 bg-gradient-to-t from-black/90 via-black/20 to-transparent opacity-80 group-hover:opacity-100 transition-opacity duration-500"></div>
                </div>
                <div class="absolute bottom-0 left-0 p-8 w-full z-10 text-white translate-y-4 group-hover:translate-y-0 transition-transform duration-500">
                    <div class="w-12 h-12 rounded-full bg-white/10 backdrop-blur-md flex items-center justify-center mb-6 border border-white/20">
                        <span class="material-symbols-outlined text-2xl text-primary">healing</span>
                    </div>
                    <h3 class="text-3xl font-display mb-2">Reabilitação</h3>
                    <p class="text-sm text-white/80 opacity-0 group-hover:opacity-100 transition-opacity duration-500 delay-100 flex items-center gap-2">
                        Ver detalhes <span class="material-symbols-outlined text-sm">arrow_forward</span>
                    </p>
                </div>
            </div>
        </div>"""

pattern_services = re.compile(r'<div class="flex flex-col gap-8 md:gap-12 px-4 md:px-8 pb-12">.*?</div>\s*</section>', re.DOTALL)
html = pattern_services.sub(new_services_html + '\n    </section>', html)

# Replacement 2: Inject Modal HTML before </body>
modal_html = """
    <!-- Service Modal Backdrop -->
    <div id="serviceModal" class="fixed inset-0 z-[100] flex items-center justify-center p-4 sm:p-6 opacity-0 pointer-events-none transition-opacity duration-500 bg-background-dark/80 backdrop-blur-sm" onclick="handleModalClick(event)">
        <!-- Modal Content -->
        <div id="serviceModalContent" class="relative w-full max-w-4xl bg-background-light dark:bg-neutral-dark rounded-3xl overflow-hidden shadow-2xl transform scale-95 translate-y-4 transition-all duration-500 flex flex-col md:flex-row border border-neutral-200 dark:border-white/10">
            <button class="absolute top-4 right-4 z-20 w-10 h-10 bg-black/20 hover:bg-black/40 text-white rounded-full flex items-center justify-center backdrop-blur-md transition-colors" onclick="closeServiceModal()">
                <span class="material-symbols-outlined">close</span>
            </button>
            <div id="modalImage" class="w-full md:w-5/12 h-64 md:h-auto bg-cover bg-center relative">
                <div class="absolute inset-0 bg-gradient-to-r from-transparent to-background-light dark:to-neutral-dark opacity-10 md:opacity-100"></div>
            </div>
            <div class="w-full md:w-7/12 p-8 md:p-12 flex flex-col justify-center bg-background-light dark:bg-neutral-dark">
                <div class="flex items-center gap-4 mb-6">
                    <div class="w-12 h-12 rounded-full bg-primary/20 flex items-center justify-center">
                        <span id="modalIcon" class="material-symbols-outlined text-2xl text-primary"></span>
                    </div>
                    <h3 id="modalTitle" class="text-3xl md:text-4xl font-display font-medium text-text-main dark:text-white"></h3>
                </div>
                <p id="modalDescription" class="text-neutral-600 dark:text-neutral-300 text-lg leading-relaxed mb-8 font-light"></p>
                <button onclick="sendModalWhatsApp()" class="group w-full flex items-center justify-center gap-3 bg-[#25D366] hover:bg-[#20bd5a] text-white font-bold py-4 px-6 rounded-xl transition-all shadow-lg hover:shadow-xl transform hover:-translate-y-1">
                    <svg class="bi bi-whatsapp w-6 h-6" fill="currentColor" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
                        <path d="M13.601 2.326A7.854 7.854 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.933 7.933 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.898 7.898 0 0 0 13.6 2.326zM7.994 14.521a6.573 6.573 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.557 6.557 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592zm3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.729.729 0 0 0-.529.247c-.182.198-.691.677-.691 1.654 0 .977.71 1.916.81 2.049.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232z"></path>
                    </svg>
                    <span>Quero agendar via WhatsApp</span>
                </button>
            </div>
        </div>
    </div>
</body>"""

html = html.replace('</body>', modal_html)

# Replacement 3: Inject JS Script before </script> at the end
js_html = """
        // Service Data for Modals
        const serviceData = {
            'classico': {
                title: 'Pilates Clássico',
                icon: 'self_improvement',
                image: 'pilates_classico.png',
                desc: 'O método original criado por Joseph Pilates é focado na contrologia. O Pilates Clássico exige precisão, controle e fluidez. Utilizando equipamentos desenhados especificamente para isso, o método promove um alinhamento postural perfeito, ganho expressivo de força muscular, e flexibilidade incomparável.\\n\\nAqui no Studio RL, seguimos a tradição à risca para que você sinta todos os benefícios de um corpo em pleno funcionamento, forte e focado.'
            },
            'gestantes': {
                title: 'Gestantes',
                icon: 'pregnant_woman',
                image: 'pilates_gestantes.png',
                desc: 'Nosso programa voltado para gestantes oferece o suporte e o cuidado que essa fase tão mágica e delicada exige.\\n\\nFocamos em exercícios que fortalecem o assoalho pélvico, aliviam dores lombares e melhoram a circulação, preparando o corpo tanto para o parto quanto para o período pós-parto, garantindo a sua saúde e a do bebê.'
            },
            'reabilitacao': {
                title: 'Reabilitação',
                icon: 'healing',
                image: 'pilates_reabilitacao.png',
                desc: 'Combinamos os princípios do Pilates com a expertise em fisioterapia para criar um ambiente seguro e 100% voltado para a sua recuperação.\\n\\nSeja para tratar dores crônicas, recuperação pós-cirúrgica ou lesões articulares, nosso método devolve a funcionalidade e o controle corporal sem impacto.'
            }
        };

        let currentServiceTitle = '';

        function openServiceModal(serviceKey) {
            const data = serviceData[serviceKey];
            if(!data) return;

            currentServiceTitle = data.title;
            document.getElementById('modalTitle').innerText = data.title;
            document.getElementById('modalIcon').innerText = data.icon;
            document.getElementById('modalImage').style.backgroundImage = `url('${data.image}')`;
            
            // Format line breaks
            document.getElementById('modalDescription').innerHTML = data.desc.replace(/\\n/g, '<br/>');

            const modal = document.getElementById('serviceModal');
            const content = document.getElementById('serviceModalContent');
            
            modal.classList.remove('opacity-0', 'pointer-events-none');
            content.classList.remove('scale-95', 'translate-y-4');
        }

        function closeServiceModal() {
            const modal = document.getElementById('serviceModal');
            const content = document.getElementById('serviceModalContent');
            
            content.classList.add('scale-95', 'translate-y-4');
            modal.classList.add('opacity-0', 'pointer-events-none');
        }

        function handleModalClick(e) {
            if(e.target.id === 'serviceModal') {
                closeServiceModal();
            }
        }

        function sendModalWhatsApp() {
            const msg = `Olá, Dra. Rhaisa! Tudo bem? Gostaria de saber mais sobre *${currentServiceTitle}*.`;
            window.open(`https://wa.me/5583999999999?text=${encodeURIComponent(msg)}`, '_blank');
        }
    </script>"""

html = html.replace('    </script>\n</body>', js_html + '\n</body>')

with open('landing_page.html', 'w', encoding='utf-8') as f:
    f.write(html)
