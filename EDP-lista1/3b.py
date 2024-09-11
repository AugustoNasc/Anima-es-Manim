from manim import *

class PDEWaveEquationB(Scene):
    def construct(self):
        # Texto e equação separados
        title_text = Tex("Solução da equação:")  # Parte textual
        equation = MathTex(r"u_t + 4u_x = 0, \, u(0, t) = \sin(3t)")  # Parte matemática
        
        # Ajustar as posições
        title_text.to_edge(UP)
        equation.next_to(title_text, DOWN)  # Posiciona a equação abaixo do texto
        
        # Adicionar os elementos na cena
        self.play(Write(title_text))
        self.play(Write(equation))
        
        # Escrever a resolução:
        resolution = Tex("Daí, pelo método das características, temos:")
        equation_2 = MathTex(r"\left\{\begin{array}{l}\dfrac{d}{da}t = 1 \\\dfrac{d}{da}x = 4 \\\dfrac{d}{da}u = 0\end{array}\right.")  # Parte matemática
        
        resolution.next_to(equation, DOWN)
        equation_2.next_to(resolution, DOWN)

        self.play(Write(resolution))
        self.play(Write(equation_2))
        self.wait(1)

        # Deslocar equation_2 para a esquerda
        self.play(equation_2.animate.shift(LEFT * 2))  # Move equation_2 para a esquerda

        # Criar a seta Rightarrow
        arrow = MathTex(r"\Rightarrow")
        arrow.next_to(equation_2, RIGHT)  # Posiciona a seta à direita de equation_2
        self.play(Write(arrow))

        # Nova equação
        new_equation_2 = MathTex(r"\left\{\begin{array}{l}t(s,a) = a + s \\x(s,a) = 4a \\u(s,a) = \sin(3s)\end{array}\right.")  # Parte matemática
        new_equation_2.next_to(arrow, RIGHT)  # Cópia de equation_2
        self.wait(1)
        self.play(Write(new_equation_2))

        resolution = Tex("Foi escolhido esse s e a arbitariamente, \\\\já que temos a informação que u(0,t) = sin(3t).")
        
        resolution.next_to(new_equation_2, 3.5*DOWN)
        resolution.shift(1.5*LEFT)
        self.play(Write(resolution))

        # Esperar um pouco para visualizar o resultado
        self.wait(2)

        # Criar um grupo com todos os objetos na cena
        all_objects = Group(*self.mobjects)
        
        # Limpar a tela com uma transição suave (fade out) de todos os objetos
        self.play(FadeOut(all_objects))
        self.wait(0.5)

        # Texto e equação separados
        title_text_2 = Tex("Assim,")  # Parte textual
        equation_2 = MathTex(r"\left\{\begin{array}{l}4t=4a+4s \\x = 4a \end{array}\right.")  # Parte matemática
        
        # Ajustar as posições
        title_text_2.to_edge(UP)
        equation_2.next_to(title_text_2, DOWN)  # Posiciona a equação abaixo do texto

        # Adicionar os elementos na cena
        self.play(Write(title_text_2))
        self.play(Write(equation_2))

        # Deslocar equation_2 para a esquerda
        self.play(equation_2.animate.shift(LEFT * 2))  # Move equation_2 para a esquerda

        # Criar a seta Rightarrow
        arrow = MathTex(r"\Rightarrow")
        arrow.next_to(equation_2, RIGHT)  # Posiciona a seta à direita de equation_2
        self.play(Write(arrow))

        # Nova equação
        new_equation_2 = MathTex(r"s=\dfrac{4t-x}{4}")  # Parte matemática
        new_equation_2.next_to(arrow, RIGHT)  # Cópia de equation_2
        self.wait(1)
        self.play(Write(new_equation_2))

        # Limpar a tela novamente
        self.play(FadeOut(Group(title_text_2, equation_2, new_equation_2, arrow)))
        self.wait(0.5)

        # Texto e equação separados
        title_text_3 = Tex("Por fim, sabemos, então, que")  # Parte textual
        equation_3 = MathTex(r"u(x,t)=\sin(3s)=\sin\left(3\left(t-\frac{x}{4}\right)\right)")  # Parte matemática
        
        # Ajustar as posições
        title_text_3.to_edge(UP)
        equation_3.next_to(title_text_3, DOWN)  # Posiciona a equação abaixo do texto
        equation_3.shift(0.4*LEFT)
        
        # Adicionar os elementos na cena
        self.play(Write(title_text_3))
        self.play(Write(equation_3))

        self.wait(10)
