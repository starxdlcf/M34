from manim import *
import numpy as np
 
# ─────────────────────────────────────────────
#  PALETA DE CORES  (inspirada em design moderno)
# ─────────────────────────────────────────────
AZUL_CLARO   = "#4FC3F7"
AZUL_ESCURO  = "#1565C0"
VERDE        = "#66BB6A"
LARANJA      = "#FFA726"
ROSA         = "#F06292"
AMARELO      = "#FFD54F"
CINZA_FUNDO  = "#1A1A2E"   # fundo escuro elegante
BRANCO       = "#F5F5F5"
LILAS        = "#CE93D8"
 
 
# ╔══════════════════════════════════════════╗
# ║  CENA 1 – Título e apresentação          ║
# ╚══════════════════════════════════════════╝
class Cena1_Titulo(Scene):
    def construct(self):
        self.camera.background_color = CINZA_FUNDO
 
        titulo = Text("Fórmula de Heron", font_size=64,
                      color=AZUL_CLARO, weight=BOLD)
        subtitulo = Text(
            "Como calcular a área de um triângulo\napenas com seus três lados",
            font_size=28, color=BRANCO, line_spacing=1.4
        ).next_to(titulo, DOWN, buff=0.5)
        autor = Text("— Séc. I d.C., Alexandria —",
                     font_size=22, color=LILAS, slant=ITALIC
                     ).next_to(subtitulo, DOWN, buff=0.5)
 
        grupo = VGroup(titulo, subtitulo, autor).move_to(ORIGIN)
 
        self.play(Write(titulo), run_time=1.8)
        self.play(FadeIn(subtitulo, shift=UP * 0.3), run_time=1.2)
        self.play(FadeIn(autor, shift=UP * 0.2), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(grupo))
 
 
# ╔══════════════════════════════════════════╗
# ║  CENA 2 – O triângulo e seus lados       ║
# ╚══════════════════════════════════════════╝
class Cena2_Triangulo(Scene):
    def construct(self):
        self.camera.background_color = CINZA_FUNDO
 
        # ── Vértices do triângulo (a=5, b=6, c=7) ──
        a, b, c = 5, 6, 7
        # Posicionamento dos vértices em coordenadas
        A = np.array([-3.0, -1.5, 0])
        B = np.array([ 2.0, -1.5, 0])
        C = np.array([-0.2,  2.0, 0])
 
        tri = Polygon(A, B, C,
                      color=AZUL_CLARO,
                      stroke_width=3,
                      fill_color=AZUL_ESCURO,
                      fill_opacity=0.25)
 
        # ── Rótulos dos lados ──
        mid_AB = (A + B) / 2
        mid_BC = (B + C) / 2
        mid_CA = (C + A) / 2
 
        rot_c = MathTex("c = 5", color=LARANJA, font_size=36
                        ).move_to(mid_AB + np.array([0, -0.45, 0]))
        rot_a = MathTex("a = 6", color=VERDE, font_size=36
                        ).move_to(mid_BC + np.array([0.5, 0, 0]))
        rot_b = MathTex("b = 7", color=ROSA, font_size=36
                        ).move_to(mid_CA + np.array([-0.55, 0, 0]))
 
        # ── Rótulos dos vértices ──
        vA = Text("A", font_size=28, color=BRANCO).move_to(A + np.array([-0.35, -0.35, 0]))
        vB = Text("B", font_size=28, color=BRANCO).move_to(B + np.array([0.35, -0.35, 0]))
        vC = Text("C", font_size=28, color=BRANCO).move_to(C + np.array([0, 0.38, 0]))
 
        pergunta = Text(
            "Como encontrar a área sem conhecer a altura?",
            font_size=28, color=AMARELO
        ).to_edge(UP, buff=0.5)
 
        self.play(Write(pergunta), run_time=1.5)
        self.play(Create(tri), run_time=1.8)
        self.play(FadeIn(vA, vB, vC))
        self.play(
            Write(rot_c), Write(rot_a), Write(rot_b),
            run_time=1.5
        )
        self.wait(2)
 
        # ── Seta apontando para os lados ──
        destaque = Text("Apenas estes três valores!",
                        font_size=26, color=LILAS).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(destaque, shift=UP * 0.2))
        self.wait(2)
        self.play(FadeOut(VGroup(tri, rot_a, rot_b, rot_c, vA, vB, vC,
                                 pergunta, destaque)))
 
 
# ╔══════════════════════════════════════════╗
# ║  CENA 3 – Semiperímetro                  ║
# ╚══════════════════════════════════════════╝
class Cena3_Semimetro(Scene):
    def construct(self):
        self.camera.background_color = CINZA_FUNDO
 
        titulo = Text("Passo 1 — O Semiperímetro  (p)",
                      font_size=38, color=AZUL_CLARO, weight=BOLD
                      ).to_edge(UP, buff=0.6)
        self.play(Write(titulo))
 
        # ── Explicação visual ──
        explicacao = Text(
            "Imagine que você enrola um barbante ao redor\n"
            "do triângulo e depois dobra ao meio.",
            font_size=28, color=BRANCO, line_spacing=1.5
        ).next_to(titulo, DOWN, buff=0.5)
        self.play(FadeIn(explicacao, shift=UP * 0.2))
        self.wait(2)
 
        # ── Fórmula do semiperímetro ──
        formula_p = MathTex(
            r"p = \frac{a + b + c}{2}",
            font_size=56, color=AMARELO
        ).next_to(explicacao, DOWN, buff=0.7)
 
        self.play(Write(formula_p), run_time=1.8)
        self.wait(0.8)
 
        # ── Exemplo numérico ──
        exemplo = MathTex(
            r"p = \frac{6 + 7 + 5}{2} = \frac{18}{2} = 9",
            font_size=46, color=VERDE
        ).next_to(formula_p, DOWN, buff=0.6)
 
        self.play(Write(exemplo), run_time=1.8)
        self.wait(2.5)
        self.play(FadeOut(VGroup(titulo, explicacao, formula_p, exemplo)))
 
 
# ╔══════════════════════════════════════════╗
# ║  CENA 4 – Derivação / intuição geométrica║
# ╚══════════════════════════════════════════╝
class Cena4_Intuicao(Scene):
    def construct(self):
        self.camera.background_color = CINZA_FUNDO
 
        titulo = Text("Por dentro da fórmula — intuição geométrica",
                      font_size=32, color=AZUL_CLARO, weight=BOLD
                      ).to_edge(UP, buff=0.5)
        self.play(Write(titulo))
 
        # ── Cada fator destacado ──
        fator_titulo = Text(
            "A fórmula é um produto de quatro 'distâncias ao semiperímetro':",
            font_size=25, color=BRANCO
        ).next_to(titulo, DOWN, buff=0.5)
        self.play(FadeIn(fator_titulo))
 
        fatores = VGroup(
            MathTex(r"p",       font_size=48, color=AMARELO),
            MathTex(r"(p - a)", font_size=48, color=VERDE),
            MathTex(r"(p - b)", font_size=48, color=ROSA),
            MathTex(r"(p - c)", font_size=48, color=LARANJA),
        ).arrange(RIGHT, buff=0.9).next_to(fator_titulo, DOWN, buff=0.7)
 
        for f in fatores:
            self.play(GrowFromCenter(f), run_time=0.5)
        self.wait(1)
 
        # ── Significado de cada fator ──
        desc = VGroup(
            Text("Semiperímetro total",     font_size=20, color=AMARELO),
            Text("Quanto 'sobra' do lado a", font_size=20, color=VERDE),
            Text("Quanto 'sobra' do lado b", font_size=20, color=ROSA),
            Text("Quanto 'sobra' do lado c",  font_size=20, color=LARANJA),
        )
        for i, d in enumerate(desc):
            d.next_to(fatores[i], DOWN, buff=0.3)
            self.play(FadeIn(d, shift=UP * 0.15), run_time=0.4)
 
        self.wait(2)
 
        nota = Text(
            "Se qualquer lado fosse igual a p, a área seria zero —\n"
            "o triângulo colapsaria numa linha reta!",
            font_size=24, color=LILAS, line_spacing=1.4
        ).to_edge(DOWN, buff=0.7)
        self.play(Write(nota), run_time=1.5)
        self.wait(3)
        self.play(FadeOut(VGroup(titulo, fator_titulo, fatores, desc, nota)))
 
 
# ╔══════════════════════════════════════════╗
# ║  CENA 5 – A fórmula completa animada     ║
# ╚══════════════════════════════════════════╝
class Cena5_Formula(Scene):
    def construct(self):
        self.camera.background_color = CINZA_FUNDO
 
        titulo = Text("A Fórmula de Heron",
                      font_size=44, color=AZUL_CLARO, weight=BOLD
                      ).to_edge(UP, buff=0.6)
        self.play(Write(titulo))
 
        formula = MathTex(
            r"A = \sqrt{p(p-a)(p-b)(p-c)}",
            font_size=64,
            substrings_to_isolate=["A", "p", "(p-a)", "(p-b)", "(p-c)"]
        )
        formula.set_color_by_tex("A",     BRANCO)
        formula.set_color_by_tex("p",     AMARELO)
        formula.set_color_by_tex("(p-a)", VERDE)
        formula.set_color_by_tex("(p-b)", ROSA)
        formula.set_color_by_tex("(p-c)", LARANJA)
        formula.next_to(titulo, DOWN, buff=0.9)
 
        self.play(Write(formula), run_time=2.5)
        self.wait(1)
 
        # ── Caixa de destaque ──
        caixa = SurroundingRectangle(formula,
                                     color=AZUL_CLARO,
                                     buff=0.25,
                                     corner_radius=0.2)
        self.play(Create(caixa))
        self.wait(1.5)
 
        # ── Aplicação numérica passo a passo ──
        passo1 = MathTex(r"a=6,\ b=7,\ c=5 \quad\Rightarrow\quad p=9",
                         font_size=36, color=BRANCO
                         ).next_to(formula, DOWN, buff=0.9)
        passo2 = MathTex(
            r"A = \sqrt{9 \cdot (9-6) \cdot (9-7) \cdot (9-5)}",
            font_size=36, color=BRANCO
        ).next_to(passo1, DOWN, buff=0.4)
        passo3 = MathTex(
            r"A = \sqrt{9 \cdot 3 \cdot 2 \cdot 4} = \sqrt{216} \approx 14{,}70",
            font_size=36, color=VERDE
        ).next_to(passo2, DOWN, buff=0.4)
 
        self.play(FadeIn(passo1, shift=UP * 0.2))
        self.wait(0.8)
        self.play(FadeIn(passo2, shift=UP * 0.2))
        self.wait(0.8)
        self.play(FadeIn(passo3, shift=UP * 0.2))
        self.wait(3)
        self.play(FadeOut(VGroup(titulo, formula, caixa, passo1, passo2, passo3)))
 
 
# ╔══════════════════════════════════════════╗
# ║  CENA 6 – Triângulo com área preenchida  ║
# ╚══════════════════════════════════════════╝
class Cena6_AreaVisual(Scene):
    def construct(self):
        self.camera.background_color = CINZA_FUNDO
 
        titulo = Text("Visualizando a área calculada",
                      font_size=38, color=AZUL_CLARO, weight=BOLD
                      ).to_edge(UP, buff=0.5)
        self.play(Write(titulo))
 
        # ── Triângulo (mesmo das cenas anteriores) ──
        A = np.array([-2.8, -1.8, 0])
        B = np.array([ 2.2, -1.8, 0])
        C = np.array([-0.2,  1.8, 0])
 
        contorno = Polygon(A, B, C, color=AZUL_CLARO, stroke_width=3)
        preenchimento = Polygon(A, B, C,
                                fill_color=AZUL_ESCURO,
                                fill_opacity=0,
                                stroke_opacity=0)
 
        rot_c = MathTex("c=5", color=LARANJA, font_size=30
                        ).move_to((A+B)/2 + np.array([0, -0.4, 0]))
        rot_a = MathTex("a=6", color=VERDE, font_size=30
                        ).move_to((B+C)/2 + np.array([0.55, 0, 0]))
        rot_b = MathTex("b=7", color=ROSA, font_size=30
                        ).move_to((C+A)/2 + np.array([-0.55, 0, 0]))
 
        self.play(Create(contorno), run_time=1.5)
        self.play(Write(rot_a), Write(rot_b), Write(rot_c))
 
        # ── Anima o preenchimento gradual ──
        preenchimento.set_fill(opacity=0)
        preenchimento.set_stroke(opacity=0)
        self.add(preenchimento)
 
        area_label = MathTex(r"A \approx 14{,}70",
                             font_size=44, color=AMARELO
                             ).to_edge(RIGHT, buff=1.2)
 
        self.play(
            preenchimento.animate.set_fill(AZUL_CLARO, opacity=0.45),
            run_time=2
        )
        self.play(Write(area_label))
 
        # ── Linha da altura (para mostrar que NÃO precisamos dela) ──
        foot = np.array([-0.2, -1.8, 0])
        altura_line = DashedLine(C, foot, color=LILAS, dash_length=0.15)
        altura_label = MathTex(r"h\ ?", color=LILAS, font_size=30
                               ).next_to(altura_line, RIGHT, buff=0.15)
        nao_precisa = Text("Não precisamos da altura!",
                           font_size=24, color=LILAS
                           ).next_to(altura_label, RIGHT, buff=0.3)
 
        self.play(Create(altura_line), Write(altura_label))
        self.play(FadeIn(nao_precisa, shift=LEFT * 0.2))
        self.wait(3)
        self.play(FadeOut(VGroup(
            titulo, contorno, preenchimento,
            rot_a, rot_b, rot_c,
            area_label, altura_line, altura_label, nao_precisa
        )))
 
 
# ╔══════════════════════════════════════════╗
# ║  CENA 7 – Conclusão                      ║
# ╚══════════════════════════════════════════╝
class Cena7_Conclusao(Scene):
    def construct(self):
        self.camera.background_color = CINZA_FUNDO
 
        titulo = Text("Resumo", font_size=52,
                      color=AZUL_CLARO, weight=BOLD)
        self.play(Write(titulo))
        self.play(titulo.animate.to_edge(UP, buff=0.5))
 
        passos = VGroup(
            Text("1.  Meça os três lados: a, b e c",
                 font_size=30, color=BRANCO),
            MathTex(r"2.\ \ p = \dfrac{a+b+c}{2}",
                    font_size=34, color=AMARELO),
            MathTex(r"3.\ \ A = \sqrt{p(p-a)(p-b)(p-c)}",
                    font_size=36, color=VERDE),
            Text("4.  Pronto! — sem precisar da altura.",
                 font_size=30, color=BRANCO),
        ).arrange(DOWN, buff=0.55, aligned_edge=LEFT
                  ).next_to(titulo, DOWN, buff=0.7).shift(LEFT * 0.5)
 
        for p in passos:
            self.play(FadeIn(p, shift=RIGHT * 0.3), run_time=0.7)
            self.wait(0.6)
 
        self.wait(1.5)
 
        heron = Text(
            '"A geometria é a arte de raciocinar\ncorretamente sobre figuras incorretas."',
            font_size=24, color=LILAS, slant=ITALIC, line_spacing=1.4
        ).to_edge(DOWN, buff=0.8)
        self.play(Write(heron), run_time=2)
        self.wait(4)
        self.play(FadeOut(VGroup(titulo, passos, heron)))
 
 
# ╔══════════════════════════════════════════╗
# ║  CENA COMPLETA (une todas as cenas)      ║
# ╚══════════════════════════════════════════╝
class FormulaDeHeron(Scene):
    """
    Rode esta classe para gerar o vídeo completo:
        manim -pqh formula_de_heron.py FormulaDeHeron
    """
    def construct(self):
        cenas = [
            Cena1_Titulo,
            Cena2_Triangulo,
            Cena3_Semimetro,
            Cena4_Intuicao,
            Cena5_Formula,
            Cena6_AreaVisual,
            Cena7_Conclusao,
        ]
        for CenaClass in cenas:
            cena = CenaClass()
            cena.camera = self.camera
            cena.renderer = self.renderer
            cena.construct()