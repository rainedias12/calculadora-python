# Importa as classes necessárias do Kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# Define a classe principal do aplicativo, que herda de App
class MainApp(App):
    # O método build é onde a interface do usuário é construída
    def build(self):
        # Lista de operadores matemáticos
        self.operators = ["/", "*", "+", "-"]
        # Variáveis de controle para o estado da calculadora
        self.last_was_operator = None # Indica se o último botão pressionado foi um operador
        self.last_button = None       # Armazena o texto do último botão pressionado

        # Cria o layout principal vertical para a calculadora
        main_layout = BoxLayout(orientation="vertical")

        # Cria o campo de texto onde a expressão e o resultado serão exibidos
        self.solution = TextInput(
            multiline=False,  # Apenas uma linha de texto
            readonly=True,    # O usuário não pode digitar diretamente
            halign="right",   # Alinhamento do texto à direita
            font_size=55      # Tamanho da fonte
        )
        # Adiciona o campo de texto ao layout principal
        main_layout.add_widget(self.solution)

        # Define os botões da calculadora em uma matriz
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]

        # Itera sobre as linhas de botões para criá-los
        for row in buttons:
            # Cria um layout horizontal para cada linha de botões
            h_layout = BoxLayout()
            # Itera sobre os rótulos de cada botão na linha
            for label in row:
                # Cria um botão com o texto e dicas de posição
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                # Associa a função on_button_press ao evento de pressionar o botão
                button.bind(on_press=self.on_button_press)
                # Adiciona o botão ao layout horizontal da linha
                h_layout.add_widget(button)
            # Adiciona o layout horizontal (linha de botões) ao layout principal
            # CORREÇÃO: Esta linha foi movida para fora do loop interno para adicionar todas as linhas.
            main_layout.add_widget(h_layout)

        # Cria o botão de igual (=) separadamente
        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        # Associa a função on_solution ao evento de pressionar o botão de igual
        equals_button.bind(on_press=self.on_solution)
        # Adiciona o botão de igual ao layout principal
        # CORREÇÃO: Esta linha foi movida para fora do loop de botões.
        main_layout.add_widget(equals_button)

        # Retorna o layout principal para ser exibido como a interface do aplicativo
        # CORREÇÃO: Esta linha foi movida para o final do método build.
        return main_layout

    # Método chamado quando um botão numérico ou de operador é pressionado
    # CORREÇÃO: Este método foi indentado corretamente dentro da classe MainApp.
    def on_button_press(self, instance):
        current = self.solution.text  # Pega o texto atual no campo de solução
        button_text = instance.text   # Pega o texto do botão que foi pressionado

        # Se o botão pressionado for "C" (Clear)
        if button_text == "C":
            self.solution.text = ""  # Limpa o campo de solução
        else:
            # Evita que dois operadores sejam digitados consecutivamente (ex: "++", "*-")
            if current and (self.last_was_operator and button_text in self.operators):
                return
            # Evita que a expressão comece com um operador
            elif current == "" and button_text in self.operators:
                return
            else:
                # Adiciona o texto do botão à expressão atual
                new_text = current + button_text
                self.solution.text = new_text
            # Atualiza o último botão pressionado e se ele era um operador
            self.last_button = button_text
            self.last_was_operator = self.last_button in self.operators

    # Método chamado quando o botão de igual (=) é pressionado
    # CORREÇÃO: Este método foi indentado corretamente dentro da classe MainApp.
    def on_solution(self, instance):
        text = self.solution.text  # Pega a expressão atual no campo de solução
        if text:
            try:
                # Usa eval() para calcular o resultado da expressão
                # ATENÇÃO: eval() pode ser perigoso com entradas não confiáveis,
                # mas para uma calculadora simples como esta, é aceitável.
                solution = str(eval(self.solution.text))
                self.solution.text = solution  # Exibe o resultado
            except Exception as e:
                self.solution.text = "Error"  # Exibe "Error" em caso de erro de cálculo
                print(f"Calculation error: {e}") # Imprime o erro no console para depuração

# Garante que o aplicativo só seja executado quando o script for o principal
if __name__ == "__main__":
    MainApp().run() # Inicia o aplicativo Kivylution