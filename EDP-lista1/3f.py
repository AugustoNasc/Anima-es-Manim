from manim import *

class PDEWaveEquationF(Scene):
    def construct(self):
        # Texto e equação separados
        title_text = Tex("Solução da equação:")  # Parte textual
        equation = MathTex(r"x^2u_x + y^2u_y = 4, \, u\left(x, \dfrac{x}{x-1}\right) = 4")  # Parte matemática
        
        # Ajustar as posições
        title_text.to_edge(UP)
        equation.next_to(title_text, DOWN)  # Posiciona a equação abaixo do texto
        
        # Adicionar os elementos na cena
        self.play(Write(title_text))
        self.play(Write(equation))
        
        # Escrever a resolução:
        resolution = Tex("Daí, pelo método das características, temos:")  # Texto explicativo
        equation_2 = MathTex(r"\left\{\begin{array}{l} \dfrac{d}{dt}x = x^2 \\\dfrac{d}{dt}y = y^2 \\\dfrac{d}{dt}u = 4 \end{array}\right.")  # Equações diferenciais
        
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
        new_equation_2 = MathTex(r"\left\{\begin{array}{l}-\dfrac{1}{x}=t-\dfrac{1}{s} \\-\dfrac{1}{y}=t-1+\dfrac{1}{s}\\u(a, s) = 4t+1\end{array}\right.")  # Parte matemática
        new_equation_2.next_to(arrow, RIGHT)  # Cópia de equation_2
        self.wait(1)
        self.play(Write(new_equation_2))

        # Esperar um pouco para visualizar o resultado
        self.wait(2)

        # Criar um grupo com todos os objetos na cena
        all_objects = Group(*self.mobjects)
        
        # Limpar a tela com uma transição suave (fade out) de todos os objetos
        self.play(FadeOut(all_objects))
        self.wait(0.5)
        resolution_2 = Tex("Foi escolhido esse x e y arbitrariamente, \\\\já que temos a informação que")
        equation=MathTex(r"u\left(x, \dfrac{x}{x-1}\right) = 4")
        
        resolution_2.to_edge(UP)
        equation.next_to(resolution_2, DOWN) 
        self.play(Write(resolution_2))
        self.play(Write(equation))


        # Texto e equação separados
        title_text_2 = Tex("Assim,")  # Parte textual
        equation_2 = MathTex(r"2t=-\dfrac{1}{x}-\dfrac{1}{y}+1")  # Parte matemática
        
        # Ajustar as posições
        title_text_2.next_to(equation, DOWN)
        equation_2.next_to(title_text_2, DOWN)  # Posiciona a equação abaixo do texto

        # Adicionar os elementos na cena
        self.play(Write(title_text_2))
        self.play(Write(equation_2))

        self.wait(2)
        # Texto e equação separados
        title_text_3 = Tex("Por fim, sabemos que")  # Parte textual
        equation_3 = MathTex(r"u(x,t) =  4t+1\\\
                             =-\dfrac{2}{x}-\dfrac{2}{y}+3")  # Solução final
        
        # Ajustar as posições
        title_text_3.next_to(equation_2, DOWN)
        equation_3.next_to(title_text_3, DOWN)  # Posiciona a equação abaixo do texto
        
        # Adicionar os elementos na cena
        self.play(Write(title_text_3))
        self.play(Write(equation_3))

        self.wait(2)

        equation_4 = MathTex(r"\blacksquare")  # cqd
        equation_4.next_to(equation_3, 2*RIGHT)
        equation_4.shift(0.5*DOWN)
        self.play(Write(equation_4))
        self.wait(8)