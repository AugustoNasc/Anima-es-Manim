from manim import *

class PDEWaveEquationD(Scene):
    def construct(self):
        # Texto e equação separados
        title_text = Tex("Solução da equação:")  # Parte textual
        equation = MathTex(r"u_x + xu_y = 4u, \, u(0, y) = y^2")  # Parte matemática
        
        # Ajustar as posições
        title_text.to_edge(UP)
        equation.next_to(title_text, DOWN)  # Posiciona a equação abaixo do texto
        
        # Adicionar os elementos na cena
        self.play(Write(title_text))
        self.play(Write(equation))
        
        # Escrever a resolução:
        resolution = Tex("Daí, pelo método das características, temos:")  # Texto explicativo
        equation_2 = MathTex(r"\left\{\begin{array}{l} \dfrac{d}{dt}x = 1 \\\dfrac{d}{dt}y = x \\\dfrac{d}{dt}u = 4u \end{array}\right.")  # Equações diferenciais
        
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
        new_equation_2 = MathTex(r"\left\{\begin{array}{l}x(a, s) = t \\y(a, s) = t^2/2 + a\\u(a, s) = e^{4t}a^2\end{array}\right.")  # Parte matemática
        new_equation_2.next_to(arrow, RIGHT)  # Cópia de equation_2
        self.wait(1)
        self.play(Write(new_equation_2))

        self.wait(2)
        resolution_2 = Tex("Foi escolhido esse t e x arbitrariamente, \\\\já que temos a informação que")
        equation=MathTex(r"u(0,y) = y^2")
        
        resolution_2.next_to(new_equation_2, 3.5*DOWN)
        resolution_2.shift(2*LEFT)
        equation.next_to(resolution_2, DOWN) 
        self.play(Write(resolution_2))
        self.play(Write(equation))

        # Esperar um pouco para visualizar o resultado
        self.wait(2)

        # Criar um grupo com todos os objetos na cena
        all_objects = Group(*self.mobjects)
        
        # Limpar a tela com uma transição suave (fade out) de todos os objetos
        self.play(FadeOut(all_objects))
        self.wait(0.5)

        # Texto e equação separados
        title_text_2 = Tex("Assim,")  # Parte textual
        equation_2 = MathTex(r"a = y-x^2/2")  # Parte matemática
        
        # Ajustar as posições
        title_text_2.to_edge(UP)
        equation_2.next_to(title_text_2, DOWN)  # Posiciona a equação abaixo do texto

        # Adicionar os elementos na cena
        self.play(Write(title_text_2))
        self.play(Write(equation_2))

        self.wait(2)
        # Texto e equação separados
        title_text_3 = Tex("Por fim, sabemos que")  # Parte textual
        equation_3 = MathTex(r"u(x,t) =  e^{4t}a^2\\\
                             =e^{4x}\left(y-\dfrac{x^2}{2}\right)")  # Solução final
        
        # Ajustar as posições
        title_text_3.next_to(equation_2, DOWN)
        equation_3.next_to(title_text_3, DOWN)  # Posiciona a equação abaixo do texto
        
        # Adicionar os elementos na cena
        self.play(Write(title_text_3))
        self.play(Write(equation_3))

        self.wait(10)
