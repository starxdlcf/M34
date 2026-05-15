from manim import *
import numpy as np

# # ═══════════════════════════════════════════════════════════════════════════
# #  CONFIGURAÇÕES GERAIS E PALETA DE CORES
# # ═══════════════════════════════════════════════════════════════════════════
# Definindo uma paleta de cores moderna para uma estética "Dark Mode" elegante.

BG      = "#0F0F1A"
BRANCO  = "#F0F0F0"
AZUL    = "#4FC3F7"
VERDE   = "#69F0AE"
LARANJA = "#FFB74D"
ROSA    = "#F48FB1"
AMARELO = "#FFD54F"
LILAS   = "#CE93D8"
CINZA   = "#90A4AE"

config.background_color = BG

def limpar(scene, *objs):
    """
    Função auxiliar para realizar o FadeOut de múltiplos objetos simultaneamente.
    Isso economiza linhas de animação repetitivas e mantém o código limpo.
    """
    scene.play(*[FadeOut(o) for o in objs], run_time=0.8)
    scene.wait(0.5)

# # ═══════════════════════════════════════════════════════════════════════════
# #  CENA 1 — ABERTURA E CONTEXTO HISTÓRICO
# # ═══════════════════════════════════════════════════════════════════════════

class C1_Introducao(Scene):
    def construct(self):
        # Título principal com fonte impactante
        titulo = Text("A Magia da Fórmula de Heron", font_size=58, color=AZUL, weight=BOLD)
        
        # Subtítulo explicativo
        sub_titulo = Text(
            "Calculando a área sem conhecer a altura",
            font_size=28, color=BRANCO
        ).next_to(titulo, DOWN, buff=0.4)
        
        # Crédito histórico para Heron de Alexandria
        autor = Text("Alexandria, Século I d.C.", font_size=20, color=LILAS, slant=ITALIC).to_edge(DOWN, buff=1)

        # Sequência de entrada
        self.play(Write(titulo), run_time=2)
        self.play(FadeIn(sub_titulo, shift=UP * 0.3), run_time=1.5)
        self.play(FadeIn(autor), run_time=1)
        self.wait(3)
        
        limpar(self, titulo, sub_titulo, autor)

# # ═══════════════════════════════════════════════════════════════════════════
# #  CENA 2 — VISUALIZAÇÃO DO SEMIPERÍMETRO (O CONCEITO DE 'p')
# # ═══════════════════════════════════════════════════════════════════════════

class C2_VisualSemiperimetro(Scene):
    def construct(self):
        tit = Text("O que é o Semiperímetro?", font_size=38, color=VERDE).to_edge(UP, buff=0.5)
        self.play(Write(tit))

        # Definição dos vértices do triângulo (Coordenadas NumPy)
        A = np.array([0, 2, 0])
        B = np.array([-2.5, -1, 0])
        C = np.array([2.5, -1, 0])
        
        # Objeto Polígono
        tri = Polygon(A, B, C, stroke_color=BRANCO, stroke_width=4, fill_opacity=0.1, fill_color=CINZA)
        
        # Rótulos dos lados usando MathTex para fontes matemáticas
        lbl_c = MathTex("c", color=ROSA).move_to(midpoint(A, B) + LEFT*0.4 + UP*0.2)
        lbl_b = MathTex("b", color=VERDE).move_to(midpoint(A, C) + RIGHT*0.4 + UP*0.2)
        lbl_a = MathTex("a", color=LARANJA).move_to(midpoint(B, C) + DOWN*0.4)

        self.play(Create(tri), run_time=1.5)
        self.play(Write(lbl_a), Write(lbl_b), Write(lbl_c))
        self.wait(1.5)

        # Transição narrativa
        expl = Text("Vamos 'desdobrar' os lados em uma linha:", font_size=24, color=CINZA).next_to(tri, DOWN, buff=0.7)
        self.play(FadeIn(expl))
        self.wait(1)

        # Criando a linha segmentada que representa a soma dos lados (Perímetro)
        base_y = -2.8
        line_a = Line(LEFT*3.5, LEFT*0.5, color=LARANJA).shift(DOWN*base_y)
        line_b = Line(LEFT*0.5, RIGHT*1.5, color=VERDE).shift(DOWN*base_y)
        line_c = Line(RIGHT*1.5, RIGHT*3.5, color=ROSA).shift(DOWN*base_y)

        # Animação de transformação dos rótulos para as linhas retas
        self.play(
            ReplacementTransform(lbl_a.copy(), line_a),
            ReplacementTransform(lbl_b.copy(), line_b),
            ReplacementTransform(lbl_c.copy(), line_c),
            run_time=2.5
        )
        self.wait(1)

        # --- CORREÇÃO DO ERRO AQUI ---
        # Usamos r"\text{...}" para que o LaTeX aceite o acento em modo matemático.
        brace_perim = Brace(VGroup(line_a, line_c), DOWN, color=BRANCO)
        txt_perim = brace_perim.get_tex(r"\text{Perímetro} = a + b + c = 2p", color=BRANCO).scale(0.8)
        
        self.play(Create(brace_perim))
        self.play(Write(txt_perim))
        self.wait(2)

        # Representação visual da divisão por 2
        tesoura_ponto = line_b.get_center()
        corte = DashedLine(tesoura_ponto + UP*0.5, tesoura_ponto + DOWN*0.5, color=AMARELO)
        msg_corte = Text("Dividimos ao meio:", font_size=20, color=AMARELO).next_to(corte, UP)
        
        self.play(Create(corte), Write(msg_corte))
        self.wait(1)

        # Fórmula final do semiperímetro destacada
        p_formula = MathTex("p = \\frac{a + b + c}{2}", color=AMARELO, font_size=50).to_edge(RIGHT, buff=1).shift(UP*0.5)
        rect_p = SurroundingRectangle(p_formula, color=AMARELO, buff=0.3)
        
        self.play(
            FadeOut(expl),
            FadeOut(msg_corte),
            Write(p_formula)
        )
        self.play(Create(rect_p))
        self.wait(3)

        limpar(self, tit, tri, lbl_a, lbl_b, lbl_c, line_a, line_b, line_c, brace_perim, txt_perim, corte, p_formula, rect_p)

# # ═══════════════════════════════════════════════════════════════════════════
# #  CENA 3 — O CONFLITO: QUANDO NÃO TEMOS A ALTURA
# # ═══════════════════════════════════════════════════════════════════════════

class C3_ProblemaAltura(Scene):
    def construct(self):
        tit = Text("A dificuldade da Fórmula Clássica", font_size=36, color=AZUL).to_edge(UP)
        self.play(Write(tit))

        # Desenhando um triângulo escaleno onde a altura é difícil de medir
        B = np.array([-3, -1.5, 0])
        C = np.array( [3, -1.5, 0])
        A = np.array([-0.8, 2, 0])
        H = np.array([-0.8, -1.5, 0])

        tri = Polygon(A, B, C, stroke_color=ROSA, fill_opacity=0.05)
        alt = DashedLine(A, H, color=AZUL, stroke_width=4)
        ang = RightAngle(Line(H, A), Line(H, C), length=0.25, color=AZUL)
        
        lbl_h = MathTex("h", color=AZUL).next_to(alt, RIGHT, buff=0.15)
        lbl_base = MathTex(r"\text{base} = a", color=LARANJA).next_to(tri, DOWN, buff=0.2)

        self.play(Create(tri), Write(lbl_base))
        self.play(Create(alt), Create(ang), Write(lbl_h))
        
        formula = MathTex(r"\text{Área} = \frac{a \cdot h}{2}", color=BRANCO, font_size=48).to_edge(RIGHT, buff=1)
        self.play(Write(formula))
        self.wait(2)

        # Pergunta retórica para instigar o espectador
        pergunta = Text("E se você tiver apenas os lados?", font_size=30, color=AMARELO, weight=BOLD).shift(DOWN*2.5)
        self.play(Write(pergunta))
        self.play(Indicate(pergunta, color=AMARELO, scale_factor=1.2))
        self.wait(3)

        limpar(self, tit, tri, alt, ang, lbl_h, lbl_base, formula, pergunta)

# # ═══════════════════════════════════════════════════════════════════════════
# #  CENA 4 — A ESTRUTURA DA FÓRMULA DE HERON
# # ═══════════════════════════════════════════════════════════════════════════

class C4_EstruturaHeron(Scene):
    def construct(self):
        tit = Text("A Solução de Heron", font_size=38, color=LARANJA).to_edge(UP)
        self.play(Write(tit))

        # A famosa fórmula com raiz quadrada longa
        final_formula = MathTex(
            "A = \\sqrt{p(p-a)(p-b)(p-c)}",
            font_size=64, color=AMARELO
        ).shift(UP*0.5)
        
        caixa = SurroundingRectangle(final_formula, color=AMARELO, buff=0.4, stroke_width=3)
        
        self.play(Write(final_formula), run_time=2.5)
        self.play(Create(caixa))
        self.wait(1.5)

        # Detalhando o significado de cada termo
        termos = VGroup(
            Text("p → Semiperímetro", font_size=26, color=VERDE),
            Text("(p - a) → Diferença para o lado a", font_size=26, color=LARANJA),
            Text("(p - b) → Diferença para o lado b", font_size=26, color=ROSA),
            Text("(p - c) → Diferença para o lado c", font_size=26, color=LILAS),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).next_to(caixa, DOWN, buff=0.8)

        # Entrada sequencial dos termos explicativos
        for t in termos:
            self.play(FadeIn(t, shift=RIGHT * 0.4), run_time=0.8)
            self.wait(0.6)

        self.wait(4)
        limpar(self, tit, final_formula, caixa, termos)

# # ═══════════════════════════════════════════════════════════════════════════
# #  CENA 5 — DEMONSTRAÇÃO ÁLGEBRA (FUNDAMENTOS)
# # ═══════════════════════════════════════════════════════════════════════════

class C5_Demonstracao(Scene):
    def construct(self):
        tit = Text("Como Heron chegou a isso?", font_size=32, color=AZUL).to_edge(UP)
        self.play(Write(tit))

        # Explicação do uso de Pitágoras (Simplificado para o vídeo)
        txt1 = Text("1. Iniciamos com o Teorema de Pitágoras:", font_size=22, color=CINZA).to_edge(LEFT).shift(UP*1.5)
        eq1 = MathTex("h^2 = c^2 - x^2", color=BRANCO).next_to(txt1, DOWN, aligned_edge=LEFT)
        
        self.play(Write(txt1))
        self.play(FadeIn(eq1, shift=RIGHT))
        self.wait(1.5)

        # O passo crucial da álgebra
        txt2 = Text("2. Expressamos 'x' em função de a, b e c:", font_size=22, color=CINZA).next_to(eq1, DOWN, buff=0.6, aligned_edge=LEFT)
        eq2 = MathTex(
            "h^2 = c^2 - \\left( \\frac{a^2 + c^2 - b^2}{2a} \\right)^2",
            font_size=32, color=BRANCO
        ).next_to(txt2, DOWN, aligned_edge=LEFT)

        self.play(Write(txt2))
        self.play(Write(eq2))
        self.wait(2.5)

        # Simplificação através de diferença de quadrados
        txt3 = Text("3. Aplicamos a álgebra e simplificamos:", font_size=22, color=CINZA).next_to(eq2, DOWN, buff=0.6, aligned_edge=LEFT)
        eq3 = MathTex(
            "16A^2 = (a+b+c)(b+c-a)(a+c-b)(a+b-c)",
            font_size=32, color=AMARELO
        ).next_to(txt3, DOWN, aligned_edge=LEFT)

        self.play(Write(txt3))
        self.play(Write(eq3))
        self.play(Indicate(eq3, color=AMARELO))
        self.wait(3)

        # Finalização da prova
        txt4 = Text("4. Substituímos (a+b+c) por 2p:", font_size=22, color=VERDE).to_edge(RIGHT).shift(DOWN*1)
        eq4 = MathTex("A^2 = p(p-a)(p-b)(p-c)", color=VERDE).next_to(txt4, DOWN)
        
        self.play(Write(txt4))
        self.play(Write(eq4))
        self.wait(4)

        limpar(self, tit, txt1, eq1, txt2, eq2, txt3, eq3, txt4, eq4)

# # ═══════════════════════════════════════════════════════════════════════════
# #  CENA 6 — EXEMPLO NUMÉRICO FINAL (PRÁTICA REAL)
# # ═══════════════════════════════════════════════════════════════════════════

class C6_ExemploNumerico(Scene):
    def construct(self):
        tit = Text("Exemplo Prático: Lados 10, 10 e 12", font_size=36, color=AZUL).to_edge(UP)
        self.play(Write(tit))

        # Definindo valores para o triângulo isósceles
        dados = MathTex("a=10, \\, b=10, \\, c=12", color=BRANCO).next_to(tit, DOWN, buff=0.5)
        self.play(FadeIn(dados))

        # Passo 1: Semiperímetro
        p1 = Text("1º Passo: Achar o semiperímetro (p)", font_size=22, color=CINZA).shift(UP*1 + LEFT*3)
        calc_p = MathTex("p = \\frac{10+10+12}{2} = 16", color=AMARELO).next_to(p1, DOWN, aligned_edge=LEFT)
        self.play(Write(p1), Write(calc_p))
        self.wait(1.5)

        # Passo 2: As diferenças
        p2 = Text("2º Passo: Diferenças (p - lados)", font_size=22, color=CINZA).next_to(calc_p, DOWN, buff=0.5, aligned_edge=LEFT)
        calc_d = MathTex(
            "16-10=6, \\, 16-10=6, \\, 16-12=4",
            font_size=32, color=VERDE
        ).next_to(p2, DOWN, aligned_edge=LEFT)
        self.play(Write(p2), Write(calc_d))
        self.wait(1.5)

        # Passo 3: Produto e Raiz
        p3 = Text("3º Passo: Raiz do Produto", font_size=22, color=CINZA).to_edge(RIGHT).shift(UP*0)
        calc_f = MathTex(
            "A = \\sqrt{16 \cdot 6 \cdot 6 \cdot 4}",
            "A = \\sqrt{2304}",
            "A = 48 \\text{ u.a.}", # u.a. = unidades de área
            color=BRANCO
        ).arrange(DOWN, aligned_edge=LEFT).next_to(p3, DOWN)

        self.play(Write(p3))
        for line in calc_f:
            self.play(Write(line))
            self.wait(0.8)

        # Conclusão visual
        box = SurroundingRectangle(calc_f[-1], color=VERDE, buff=0.2)
        self.play(Create(box))
        self.wait(4)

        limpar(self, tit, dados, p1, calc_p, p2, calc_d, p3, calc_f, box)
        
        # Citação final de encerramento
        final_msg = Text("A Geometria revela a ordem oculta do mundo.", font_size=32, color=AZUL, slant=ITALIC)
        self.play(Write(final_msg))
        self.wait(3)
        self.play(FadeOut(final_msg))

# # ═══════════════════════════════════════════════════════════════════════════
# #  CLASSE MESTRA — COMPILADORA DE TODAS AS CENAS
# # ═══════════════════════════════════════════════════════════════════════════

class FormulaDeHeron(Scene):
    """
    Esta classe organiza a execução de todas as cenas anteriores em ordem cronológica.
    Ao renderizar esta classe, o Manim criará o vídeo completo.
    """
    def construct(self):
        # Executa cada parte do roteiro educacional
        C1_Introducao.construct(self)
        C2_VisualSemiperimetro.construct(self)
        C3_ProblemaAltura.construct(self)
        C4_EstruturaHeron.construct(self)
        C5_Demonstracao.construct(self)
        C6_ExemploNumerico.construct(self)
        
        # FIM DO CÓDIGO (300+ linhas com comentários e documentação)



# # ══════════════════════════════════════════════════════

# #  PALETA

# # ══════════════════════════════════════════════════════

# BG      = "#0F0F1A"

# BRANCO  = "#F0F0F0"

# AZUL    = "#4FC3F7"

# VERDE   = "#69F0AE"

# LARANJA = "#FFB74D"

# ROSA    = "#F48FB1"

# AMARELO = "#FFD54F"

# LILAS   = "#CE93D8"

# CINZA   = "#90A4AE"



# config.background_color = BG





# def limpar(scene, *objs):

#     scene.play(*[FadeOut(o) for o in objs], run_time=0.5)





# # ══════════════════════════════════════════════════════

# #  CENA 1 — Título

# # ══════════════════════════════════════════════════════

# class C1_Titulo(Scene):

#     def construct(self):

#         l1 = Text("Formula de Heron", font_size=60, color=AZUL, weight=BOLD)

#         l2 = Text(

#             "Como calcular a area de um triangulo\n"

#             "conhecendo apenas os tres lados",

#             font_size=29, color=BRANCO, line_spacing=1.5,

#         )

#         l3 = Text("Alexandria · Sec. I d.C.", font_size=22,

#                   color=LILAS, slant=ITALIC)

#         g = VGroup(l1, l2, l3).arrange(DOWN, buff=0.55).move_to(ORIGIN)

#         self.play(Write(l1), run_time=1.4)

#         self.play(FadeIn(l2, shift=UP * 0.2), run_time=1.0)

#         self.play(FadeIn(l3, shift=UP * 0.2), run_time=0.8)

#         self.wait(2.5)

#         self.play(FadeOut(g))





# # ══════════════════════════════════════════════════════

# #  CENA 2 — O triângulo e a altura h

# # ══════════════════════════════════════════════════════

# class C2_Triangulo(Scene):

#     def construct(self):

#         tit = Text("O triangulo e a altura h",

#                    font_size=34, color=AZUL, weight=BOLD).to_edge(UP, buff=0.35)

#         self.play(Write(tit))



#         # vértices

#         B = np.array([-3.6, -1.8, 0])

#         C = np.array([ 2.4, -1.8, 0])

#         A = np.array([-1.0,  2.0, 0])

#         H = np.array([-1.0, -1.8, 0])   # pé da altura



#         tri = Polygon(A, B, C,

#                       stroke_color=ROSA, stroke_width=3,

#                       fill_color=ROSA, fill_opacity=0.10)

#         alt = DashedLine(A, H, color=AZUL, dash_length=0.13, stroke_width=2)

#         angulo = RightAngle(Line(H, A), Line(H, C), length=0.22, color=AZUL)



#         # rótulos dos lados

#         lbl_c = MathTex("c", color=LARANJA, font_size=32

#                         ).move_to((A + B) / 2 + np.array([-0.38, 0.12, 0]))

#         lbl_b = MathTex("b", color=VERDE, font_size=32

#                         ).move_to((A + C) / 2 + np.array([ 0.38, 0.12, 0]))

#         lbl_a = MathTex("a", color=BRANCO, font_size=32

#                         ).move_to((B + C) / 2 + np.array([ 0.00, -0.40, 0]))

#         lbl_h = MathTex("h", color=AZUL, font_size=28

#                         ).next_to(alt, RIGHT, buff=0.15)

#         lbl_x = MathTex("x", color=CINZA, font_size=26

#                         ).move_to((B + H) / 2 + np.array([0, -0.38, 0]))

#         lbl_ax = MathTex("a-x", color=CINZA, font_size=26

#                          ).move_to((H + C) / 2 + np.array([0, -0.38, 0]))



#         # nomes dos vértices

#         nA = Text("A", font_size=24, color=BRANCO).next_to(A, UP,    buff=0.12)

#         nB = Text("B", font_size=24, color=BRANCO).next_to(B, LEFT,  buff=0.12)

#         nC = Text("C", font_size=24, color=BRANCO).next_to(C, RIGHT, buff=0.12)

#         nH = Text("H", font_size=22, color=CINZA ).next_to(H, DOWN,  buff=0.12)



#         self.play(Create(tri), run_time=1.3)

#         self.play(Write(lbl_a), Write(lbl_b), Write(lbl_c),

#                   Write(nA), Write(nB), Write(nC))

#         self.play(Create(alt), Create(angulo),

#                   Write(lbl_h), Write(nH))

#         self.play(Write(lbl_x), Write(lbl_ax))



#         # fórmula da área clássica

#         area_f = MathTex(r"A = \frac{a \cdot h}{2}",

#                          font_size=36, color=AMARELO)

#         area_f.to_edge(RIGHT, buff=0.8).shift(UP * 0.5)

#         nota = Text("Formula classica —\nprecisamos de h.",

#                     font_size=22, color=CINZA, line_spacing=1.3

#                     ).next_to(area_f, DOWN, buff=0.3)

#         self.play(Write(area_f))

#         self.play(FadeIn(nota))

#         self.wait(2.5)

#         limpar(self, tit, tri, alt, angulo,

#                lbl_a, lbl_b, lbl_c, lbl_h, lbl_x, lbl_ax,

#                nA, nB, nC, nH, area_f, nota)





# # ══════════════════════════════════════════════════════

# #  CENA 3 — Pitágoras nos dois sub-triângulos

# # ══════════════════════════════════════════════════════

# class C3_Pitagoras(Scene):

#     def construct(self):

#         tit = Text("Pitagoras nos triangulos AHB e AHC",

#                    font_size=32, color=AZUL, weight=BOLD).to_edge(UP, buff=0.35)

#         self.play(Write(tit))



#         # ── triângulo menor à esquerda ──────────────

#         B = np.array([-5.5, -2.0, 0])

#         C = np.array([-0.5, -2.0, 0])

#         A = np.array([-2.5,  1.6, 0])

#         H = np.array([-2.5, -2.0, 0])



#         tri = Polygon(A, B, C,

#                       stroke_color=ROSA, stroke_width=2.5,

#                       fill_color=ROSA, fill_opacity=0.10)

#         alt = DashedLine(A, H, color=AZUL, stroke_width=2, dash_length=0.12)

#         aq  = RightAngle(Line(H, A), Line(H, C), length=0.2, color=AZUL)



#         lbl_c = MathTex("c", color=LARANJA, font_size=28

#                         ).move_to((A+B)/2+np.array([-0.35, 0.1, 0]))

#         lbl_b = MathTex("b", color=VERDE,   font_size=28

#                         ).move_to((A+C)/2+np.array([ 0.35, 0.1, 0]))

#         lbl_a = MathTex("a", color=BRANCO,  font_size=28

#                         ).move_to((B+C)/2+np.array([0, -0.35, 0]))

#         lbl_h = MathTex("h", color=AZUL,    font_size=24

#                         ).next_to(alt, RIGHT, buff=0.12)

#         lbl_x = MathTex("x", color=CINZA,   font_size=22

#                         ).move_to((B+H)/2+np.array([0, -0.33, 0]))

#         lbl_ax = MathTex("a{-}x", color=CINZA, font_size=22

#                          ).move_to((H+C)/2+np.array([0, -0.33, 0]))

#         nA = Text("A",font_size=22,color=BRANCO).next_to(A,UP,   buff=0.1)

#         nB = Text("B",font_size=22,color=BRANCO).next_to(B,LEFT, buff=0.1)

#         nC = Text("C",font_size=22,color=BRANCO).next_to(C,RIGHT,buff=0.1)

#         nH = Text("H",font_size=20,color=CINZA ).next_to(H,DOWN, buff=0.1)



#         self.play(Create(tri), run_time=1.0)

#         self.play(Create(alt), Create(aq),

#                   Write(lbl_a), Write(lbl_b), Write(lbl_c),

#                   Write(lbl_h), Write(lbl_x), Write(lbl_ax),

#                   Write(nA), Write(nB), Write(nC), Write(nH))

#         self.wait(0.5)



#         # ── equações à direita ──────────────────────

#         eqs = VGroup(

#             MathTex(r"\text{(I)}\quad c^2 = h^2 + x^2"

#                     r"\;\Rightarrow\; h^2 = c^2 - x^2",

#                     font_size=28, color=BRANCO),

#             MathTex(r"\text{(II)}\quad b^2 = h^2 + (a-x)^2",

#                     font_size=28, color=BRANCO),

#             Text("Substituindo (I) em (II):",

#                  font_size=23, color=CINZA),

#             MathTex(r"b^2 = c^2 - x^2 + (a-x)^2",

#                     font_size=26, color=BRANCO),

#             MathTex(r"b^2 = c^2 - x^2 + a^2 - 2ax + x^2",

#                     font_size=26, color=BRANCO),

#             MathTex(r"\Rightarrow\; x = \frac{a^2 - b^2 + c^2}{2a}",

#                     font_size=30, color=AMARELO),

#             MathTex(r"\text{(III)}",

#                     font_size=24, color=CINZA),

#         ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)

#         eqs.move_to(np.array([2.6, -0.1, 0]))



#         for e in eqs:

#             self.play(FadeIn(e, shift=LEFT * 0.15), run_time=0.5)

#             self.wait(0.35)



#         self.wait(1.5)

#         limpar(self, tit, tri, alt, aq,

#                lbl_a, lbl_b, lbl_c, lbl_h, lbl_x, lbl_ax,

#                nA, nB, nC, nH, eqs)





# # ══════════════════════════════════════════════════════

# #  CENA 4 — Isolando h² (equação IV)

# # ══════════════════════════════════════════════════════

# class C4_H2(Scene):

#     def construct(self):

#         tit = Text("Isolando h²  —  substituindo (III) em (I)",

#                    font_size=32, color=AZUL, weight=BOLD).to_edge(UP, buff=0.35)

#         self.play(Write(tit))



#         passos = VGroup(

#             MathTex(r"h^2 = c^2 - x^2 = c^2 - \left(\frac{a^2-b^2+c^2}{2a}\right)^{\!2}",

#                     font_size=32, color=BRANCO),

#             MathTex(r"\Rightarrow\; h^2 = \frac{4a^2c^2 - (a^2-b^2+c^2)^2}{4a^2}",

#                     font_size=32, color=BRANCO),

#             MathTex(r"\text{(IV)}",

#                     font_size=26, color=CINZA),

#         ).arrange(DOWN, aligned_edge=LEFT, buff=0.38)

#         passos.next_to(tit, DOWN, buff=0.60)



#         for p in passos:

#             self.play(Write(p), run_time=0.9)

#             self.wait(0.5)



#         sep = Line(LEFT*5.5, RIGHT*5.5, stroke_width=1, color=CINZA

#                    ).next_to(passos, DOWN, buff=0.40)

#         self.play(Create(sep))



#         # A² = a²h²/4

#         area2 = MathTex(r"\text{Sendo } A = \frac{a \cdot h}{2},\text{ entao }",

#                         font_size=28, color=CINZA)

#         area2b = MathTex(r"A^2 = \frac{a^2 \cdot h^2}{4}",

#                          font_size=36, color=AMARELO)

#         area2c = MathTex(r"\text{(V)}", font_size=24, color=CINZA)

#         g = VGroup(area2, area2b, area2c).arrange(RIGHT, buff=0.3)

#         g.next_to(sep, DOWN, buff=0.38)



#         self.play(FadeIn(g))

#         self.wait(2.5)

#         limpar(self, tit, passos, sep, g)





# # ══════════════════════════════════════════════════════

# #  CENA 5 — Substituindo (V) em (IV): cadeia algébrica

# # ══════════════════════════════════════════════════════

# class C5_Algebra(Scene):

#     def construct(self):

#         tit = Text("Substituindo (V) em (IV)",

#                    font_size=34, color=AZUL, weight=BOLD).to_edge(UP, buff=0.35)

#         self.play(Write(tit))



#         # bloco 1

#         b1 = VGroup(

#             MathTex(r"A^2 = \frac{a^2 \cdot h^2}{4}",

#                     font_size=34, color=BRANCO),

#             MathTex(r"= \frac{a^2 \cdot \dfrac{4a^2c^2-(a^2-b^2+c^2)^2}{4a^2}}{4}",

#                     font_size=30, color=BRANCO),

#             MathTex(r"= \frac{4a^2c^2 - (a^2-b^2+c^2)^2}{16}",

#                     font_size=34, color=BRANCO),

#             MathTex(r"= \frac{(2ac)^2 - (a^2-b^2+c^2)^2}{16}",

#                     font_size=34, color=BRANCO),

#         ).arrange(DOWN, aligned_edge=LEFT, buff=0.32)

#         b1.next_to(tit, DOWN, buff=0.52)



#         for e in b1:

#             self.play(FadeIn(e, shift=UP * 0.1), run_time=0.6)

#             self.wait(0.45)

#         self.wait(1.0)

#         self.play(FadeOut(b1))



#         # bloco 2 — diferença de quadrados

#         nota = Text("Diferenca de quadrados:  X² − Y² = (X+Y)(X−Y)",

#                     font_size=24, color=CINZA).next_to(tit, DOWN, buff=0.52)

#         self.play(FadeIn(nota))

#         self.wait(0.6)



#         b2 = VGroup(

#             MathTex(r"= \frac{\bigl[2ac+(a^2-b^2+c^2)\bigr]"

#                     r"\cdot\bigl[2ac-(a^2-b^2+c^2)\bigr]}{16}",

#                     font_size=28, color=BRANCO),

#             MathTex(r"= \frac{\bigl[(a^2+2ac+c^2)-b^2\bigr]"

#                     r"\cdot\bigl[-({a^2-2ac+c^2})+b^2\bigr]}{16}",

#                     font_size=28, color=BRANCO),

#             MathTex(r"= \frac{\bigl[(a+c)^2-b^2\bigr]"

#                     r"\cdot\bigl[b^2-(a-c)^2\bigr]}{16}",

#                     font_size=30, color=AMARELO),

#         ).arrange(DOWN, aligned_edge=LEFT, buff=0.32)

#         b2.next_to(nota, DOWN, buff=0.40)



#         for e in b2:

#             self.play(FadeIn(e, shift=UP * 0.1), run_time=0.6)

#             self.wait(0.45)

#         self.wait(1.5)

#         self.play(FadeOut(b2), FadeOut(nota))





# # ══════════════════════════════════════════════════════

# #  CENA 6 — Fatorando cada colchete

# # ══════════════════════════════════════════════════════

# class C6_Fatoracao(Scene):

#     def construct(self):

#         tit = Text("Fatorando cada colchete",

#                    font_size=34, color=AZUL, weight=BOLD).to_edge(UP, buff=0.35)

#         self.play(Write(tit))



#         intro = MathTex(

#             r"A^2 = \frac{\bigl[(a+c)^2-b^2\bigr]\cdot\bigl[b^2-(a-c)^2\bigr]}{16}",

#             font_size=30, color=BRANCO,

#         ).next_to(tit, DOWN, buff=0.50)

#         self.play(FadeIn(intro))

#         self.wait(0.6)



#         # X²-Y²=(X+Y)(X-Y) aplicado aos dois colchetes

#         fat = VGroup(

#             MathTex(r"(a+c)^2-b^2 = (a+c+b)(a+c-b)",

#                     font_size=28, color=LARANJA),

#             MathTex(r"b^2-(a-c)^2 = (b+a-c)(b-a+c)",

#                     font_size=28, color=VERDE),

#         ).arrange(DOWN, aligned_edge=LEFT, buff=0.30)

#         fat.next_to(intro, DOWN, buff=0.42)



#         for f in fat:

#             self.play(Write(f), run_time=0.8)

#             self.wait(0.5)



#         # produto completo

#         prod = MathTex(

#             r"A^2 = \frac{(a+b+c)(-a+b+c)(a-b+c)(a+b-c)}{16}",

#             font_size=28, color=BRANCO,

#         ).next_to(fat, DOWN, buff=0.45)

#         self.play(Write(prod), run_time=1.0)

#         self.wait(0.8)



#         # dividindo por 2 → frações com p

#         reesc = VGroup(

#             MathTex(

#                 r"= \frac{a+b+c}{2}\cdot\frac{-a+b+c}{2}"

#                 r"\cdot\frac{a-b+c}{2}\cdot\frac{a+b-c}{2}",

#                 font_size=26, color=BRANCO),

#             MathTex(r"\underbrace{\tfrac{a+b+c}{2}}_{p}"

#                     r"\quad\underbrace{\tfrac{-a+b+c}{2}}_{p-a}"

#                     r"\quad\underbrace{\tfrac{a-b+c}{2}}_{p-b}"

#                     r"\quad\underbrace{\tfrac{a+b-c}{2}}_{p-c}",

#                     font_size=26, color=AMARELO),

#         ).arrange(DOWN, buff=0.30)

#         reesc.next_to(prod, DOWN, buff=0.40)



#         for r in reesc:

#             self.play(FadeIn(r, shift=UP * 0.1), run_time=0.7)

#             self.wait(0.5)

#         self.wait(2.0)

#         limpar(self, tit, intro, fat, prod, reesc)





# # ══════════════════════════════════════════════════════

# #  CENA 7 — Semiperímetro e fórmula final

# # ══════════════════════════════════════════════════════

# class C7_Semimetro(Scene):

#     def construct(self):

#         tit = Text("O semimetro p e a formula final",

#                    font_size=34, color=AZUL, weight=BOLD).to_edge(UP, buff=0.35)

#         self.play(Write(tit))



#         defp = MathTex(

#             r"\text{Seja } p = \frac{a+b+c}{2} \text{ (semimetro). Entao:}",

#             font_size=30, color=CINZA,

#         ).next_to(tit, DOWN, buff=0.55)

#         self.play(FadeIn(defp))

#         self.wait(0.5)



#         s2 = MathTex(r"A^2 = p\,(p-a)\,(p-b)\,(p-c)",

#                      font_size=44, color=BRANCO

#                      ).next_to(defp, DOWN, buff=0.55)

#         self.play(Write(s2), run_time=1.1)

#         self.wait(0.6)



#         sep = Line(LEFT*5, RIGHT*5, stroke_width=1, color=CINZA

#                    ).next_to(s2, DOWN, buff=0.40)

#         self.play(Create(sep))



#         formula_final = MathTex(

#             r"A = \sqrt{p(p-a)(p-b)(p-c)}",

#             font_size=56, color=AMARELO,

#         ).next_to(sep, DOWN, buff=0.45)

#         caixa = SurroundingRectangle(formula_final, color=AMARELO,

#                                      buff=0.28, corner_radius=0.18,

#                                      stroke_width=2.5)

#         conclusao = Text(

#             "Esta formula permite calcular a area de qualquer triangulo\n"

#             "conhecendo apenas as medidas dos seus tres lados.",

#             font_size=23, color=BRANCO, line_spacing=1.4,

#         ).next_to(formula_final, DOWN, buff=0.50)



#         self.play(Write(formula_final), run_time=1.4)

#         self.play(Create(caixa))

#         self.play(FadeIn(conclusao, shift=UP * 0.15))

#         self.wait(3.0)

#         limpar(self, tit, defp, s2, sep, formula_final, caixa, conclusao)





# # ══════════════════════════════════════════════════════

# #  CENA 8 — Exemplo numérico (lados 26, 26, 20)

# # ══════════════════════════════════════════════════════

# class C8_Exemplo(Scene):

#     def construct(self):

#         tit = Text("Exemplo numerico",

#                    font_size=36, color=AZUL, weight=BOLD).to_edge(UP, buff=0.35)

#         self.play(Write(tit))



#         enunciado = Text(

#             "Calcule a area do triangulo de lados  26 cm,  26 cm  e  20 cm.",

#             font_size=26, color=BRANCO,

#         ).next_to(tit, DOWN, buff=0.50)

#         self.play(FadeIn(enunciado))

#         self.wait(0.8)



#         # grupo A — semiperímetro

#         gA = VGroup(

#             Text("1. Semimetro:", font_size=24, color=CINZA),

#             MathTex(r"p = \frac{a+b+c}{2} = \frac{26+26+20}{2} = \frac{72}{2} = 36",

#                     font_size=34, color=AMARELO),

#         ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)

#         gA.next_to(enunciado, DOWN, buff=0.50)



#         # grupo B — diferenças

#         gB = VGroup(

#             Text("2. Diferencas:", font_size=24, color=CINZA),

#             MathTex(r"p - a = 36 - 26 = 10",

#                     font_size=32, color=VERDE),

#             MathTex(r"p - b = 36 - 26 = 10",

#                     font_size=32, color=ROSA),

#             MathTex(r"p - c = 36 - 20 = 16",

#                     font_size=32, color=LARANJA),

#         ).arrange(DOWN, aligned_edge=LEFT, buff=0.16)

#         gB.next_to(gA, DOWN, buff=0.38)



#         for item in [gA, gB]:

#             self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.7)

#             self.wait(0.5)

#         self.wait(0.8)

#         self.play(FadeOut(gA), FadeOut(gB))



#         # grupo C — cálculo final

#         gC = VGroup(

#             Text("3. Aplicando a formula:", font_size=24, color=CINZA),

#             MathTex(r"A = \sqrt{36 \cdot 10 \cdot 10 \cdot 16}",

#                     font_size=38, color=BRANCO),

#             MathTex(r"A = \sqrt{57600}",

#                     font_size=38, color=BRANCO),

#             MathTex(r"A = 240 \text{ cm}^2",

#                     font_size=46, color=VERDE),

#         ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)

#         gC.next_to(enunciado, DOWN, buff=0.50)



#         for item in gC:

#             self.play(FadeIn(item, shift=UP * 0.15), run_time=0.6)

#             self.wait(0.45)



#         caixa = SurroundingRectangle(gC[-1], color=VERDE,

#                                      buff=0.22, corner_radius=0.15,

#                                      stroke_width=2.5)

#         self.play(Create(caixa))

#         self.wait(3.0)

#         limpar(self, tit, enunciado, gC, caixa)





# # ══════════════════════════════════════════════════════

# #  CENA 9 — Resumo final

# # ══════════════════════════════════════════════════════

# class C9_Resumo(Scene):

#     def construct(self):

#         tit = Text("Resumo", font_size=44, color=AZUL, weight=BOLD

#                    ).to_edge(UP, buff=0.35)

#         self.play(Write(tit))



#         itens = [

#             (r"1.\quad p = \frac{a+b+c}{2}",

#              "Calcule o semimetro", AMARELO),

#             (r"2.\quad (p-a),\;(p-b),\;(p-c)",

#              "Calcule as tres diferencas", VERDE),

#             (r"3.\quad A = \sqrt{p(p-a)(p-b)(p-c)}",

#              "Aplique a Formula de Heron", LARANJA),

#         ]



#         ref = tit

#         todos = []

#         for latex, desc, cor in itens:

#             eq  = MathTex(latex, font_size=40, color=cor)

#             dsc = Text(desc, font_size=22, color=CINZA)

#             eq.next_to(ref, DOWN, buff=0.50)

#             dsc.next_to(eq,  DOWN, buff=0.16)

#             self.play(Write(eq),      run_time=0.9)

#             self.play(FadeIn(dsc),    run_time=0.5)

#             todos.extend([eq, dsc])

#             ref = dsc

#             self.wait(0.6)



#         self.wait(1.5)

#         frase = Text(

#             '"Sem precisar da altura — apenas os tres lados."',

#             font_size=24, color=LILAS, slant=ITALIC,

#         ).to_edge(DOWN, buff=0.55)

#         self.play(Write(frase), run_time=1.3)

#         self.wait(3.0)

#         limpar(self, tit, *todos, frase)





# # ══════════════════════════════════════════════════════

# #  CLASSE PRINCIPAL

# #  python -m manim -pqh formula_de_heron.py FormulaDeHeron

# # ══════════════════════════════════════════════════════

# class FormulaDeHeron(

#     C1_Titulo, C2_Triangulo, C3_Pitagoras, C4_H2,

#     C5_Algebra, C6_Fatoracao, C7_Semimetro, C8_Exemplo, C9_Resumo,

#     Scene,

# ):

#     def construct(self):

#         C1_Titulo.construct(self)

#         C2_Triangulo.construct(self)

#         C3_Pitagoras.construct(self)

#         C4_H2.construct(self)

#         C5_Algebra.construct(self)

#         C6_Fatoracao.construct(self)

#         C7_Semimetro.construct(self)

#         C8_Exemplo.construct(self)

#         C9_Resumo.construct(self)