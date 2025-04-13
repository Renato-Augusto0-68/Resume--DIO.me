print("Resumeé do aluno Renato Augusto: "); print("O playground do Azure Open AI")

print("\n Capaz de fazer implantações, registro de dados, feeedback, exportar/importar como JSON, shots(exemplos de amostras) de treino da AI.")
print("\n Implicação de significado de respostas, chat de q/a (perg e resp), segurança do sistema(via chaves de segurança), ajustes de parâmetros e funcionalidades Fine Tuned")
print("\n Então, em resumo, o playgrond age para o interamento/desenvolvimento de prompts e treino/execucção de modelos e prompts.")

print("Lembrar da palavra de ouro nisso: ESTOCÁSTICA")
print("Que é o processo do acaso. Mesmo com tudoo muito bem ajustado, por conta da arquitetura transformer, baseada em porbabilidades de tokens, o acaso vai influenciar na execução da escolha probablistíca de tokens, logo afeta na geração das respostas do prompt.")
print("Por isso, pode gerar coisas aleatórias ou imprevistas.")

print("Tiktoken é a biblioteca (criada pela Open AI) utilizada para contagem de tokens, o sistema de preivsão, baseia se em cálculos probablísticos.")
print("\n Características da preparação da IA:")

print("\n Respostas anteriores incluídas: Se trata do que o azure (via playground)vai colocar na API (Basicamente um histórico, dando contexto útil e adaptável, já que dá para escolher até quantas vão ser usadas para registro/contexto, que utiliza a quantia estabelecida na resposta máxima); \n Temperatura: escolha randômica das opções e, em conjunto com Top P, a 'criatividade e variedade' da IA \n Top P: Quantas opções de resposta e, junto da Temperatura, a 'criatividade e variedade' da IA  \n Resposta máxima: Define a quantidade máxima de tokens que podem ser utilizados na resposta  \nPenalidade por Frequência: punição, com redução das chances de um token, por ter repetido \n Penalidade por presença: A mesma coisa da por frequênica, a diferença é que age na repetição de tópico (ou seja, para evitar repetir assunto)  \nSystem Message: Instruções, contexto e 'Modus Operandi' pro modelo (modela como ele vai agir, para que e diretrizes principais)  \nStop:onde vai parar (com quantos tokens, vai parar)")
print("System message pode ser treinado via shots. Shots são como simulações de perguntas que mostram o que o modelo tem que fazer na situação, dando contexto ao modelo. Não necesariamente, somente pode ser treinado assim. Existem formas alternativas.")

print("\n Temperatura e Top P: A temperatura influencia na Randomicidade (leia-se aleatoriedade) das ligações (escolhas) de tokens. Ou seja, o quão mais ou menos randômico a escolha de tokens, logo respostas. Já o Top P, na 'variedade de tokens disponíveis', ou seja é como 'o que pode ser utilizado', abrindo mais o escopo de 'respostas possíveis'. Então, junto com a temperatura elevada, o Top P alto abre o caminho pro caos  ")
print("\n Logo, uma temperatura baixa, respostas previsíveis, deterministicas. Uma temperatura mais alta, gera mais aleatoriedade, caos, até mesmo falta de sentido. Low Top P gera uma gama de possiveis respostas menor (em quantidade), Já o Top P alto, deixa um espectro maior de respostas possíveis. ")

print("\n Então, Top P alto e Temperatura baixa dá uma caoticidade controlada, mais concisa e contida, com pouco caos, mas bem variada. Já  Top P baixo e Temp elevada, gera criatividade limitada, variedade não tão grande, mas caoticidade alta.")
print("Os dois baixos (temperatura e Top P), gera previsibilidade máxima, pelo caos baixo e variedade pequena. Já Temp e Top P altos, gera criatividade máxima, beirando até a loucura; pelo caos e variabilidade altas; e até mesmo coisas sem sentido.") 

print("Frequence penalty é o quanto vai punir repetição de token(termo), ou seja, age a favor da variedade vocabular. Enquanto a presence penalty, é punir por diversidade, ou seja, se desvia demais de temas ou não. Uma P.Penal muito alta, vai evitar fugir demais do tema, já uma baixa, vai variar muito. ")

print("Multimodal: Esses sitemas possuem capacidades além de um unico modal de operação. Um exemplo, é o famoso DALL-E, o gerador de iamgens da Open AI. Ele depende de critérios de especificação no comando: Clareza (o que se quer), especificidade (como se quer, onde usar, para que usar), contexto (detalhes do que estará na imagem) e estrutura (estruturar as informações anteriores). Todo sistetma de ia, em seu uso; em cada um dos seus modais de funções, possuem seus requerimentos básicos de funcionamento, conforme cada modelo/modal de função.")

print("Aplicações: no cueso, o professor Pablo usa como 'verificador de notícias', como chat da DIO no VScode, e o DALL-E. para ilustrar o sistema de geração de imagens. Existem muito mais formas de utilizar, claro. O único problema por trás, é o consumo de tokens e o preço gasto no uso de tokens.")