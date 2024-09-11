from manim import *

class PDEWaveEquation(Scene):
    def construct(self):
        # Texto e equação separados
        title_text = Tex("Solução da equação:")  # Parte textual
        equation = MathTex(r"u_x - 3u_y = 0, \, u(x, 0) = \cos(x)")  # Parte matemática
        
        # Ajustar as posições
        title_text.to_edge(UP)
        equation.next_to(title_text, DOWN)  # Posiciona a equação abaixo do texto
        
        # Adicionar os elementos na cena
        self.play(Write(title_text))
        self.play(Write(equation))
        
        # Escrever a resolução:
        resolution = Tex("Daí, pelo método das características, temos:")
        equation_2 = MathTex(r"\left\{\begin{array}{l}\dot{x} = 1 \\\dot{y} = -3 \\\dot{u} = 0\end{array}\right.")  # Parte matemática
        
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
        new_equation_2 = MathTex(r"\left\{\begin{array}{l}x(s,t) = t+s \\y = -3t + 0 \\u = cos (s)\end{array}\right.")  # Parte matemática
        new_equation_2.next_to(arrow, RIGHT)  # Cópia de equation_2
        self.wait(1)
        self.play(Write(new_equation_2))

        resolution = Tex("Foi escolhido esse x e esse y arbitariamente, \\\\já que\
                         temos a informação que u(x, 0) = cos(x).")
        
        resolution.next_to(new_equation_2, DOWN)
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
        equation_2 = MathTex(r"s=\dfrac{3x+y}{3}")  # Parte matemática
        
        # Ajustar as posições
        title_text_2.to_edge(UP)
        equation_2.next_to(title_text_2, DOWN)  # Posiciona a equação abaixo do texto

        # Adicionar os elementos na cena
        self.play(Write(title_text_2))
        self.play(Write(equation_2))

        # Limpar a tela novamente
        self.play(FadeOut(Group(title_text_2, equation_2)))
        self.wait(0.5)

        # Texto e equação separados
        title_text_3 = Tex("Por fim, sabemos que")  # Parte textual
        equation_3 = MathTex(r"u(x,y)=cos(s)\\\\       \Rightarrow u(x,y)=cos(\dfrac{3x+y}{3})")  # Parte matemática
        
        # Ajustar as posições
        title_text_3.to_edge(UP)
        equation_3.next_to(title_text_3, DOWN)  # Posiciona a equação abaixo do texto
        equation_3.shift(LEFT)
        
        # Adicionar os elementos na cena
        self.play(Write(title_text_3))
        self.play(Write(equation_3))

        self.wait(10)
