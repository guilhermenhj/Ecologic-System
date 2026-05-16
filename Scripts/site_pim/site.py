import streamlit as st
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import csv
import os

# Configuração da página
st.set_page_config(
    page_title="EcoLogic Systems",
    page_icon="🌱",
    layout="wide"
)

# Estilo
st.markdown("""
    <style>
        .rodape {
            background-color: #2e7d32;
            color: white;
            text-align: center;
            padding: 15px;
            margin-top: 40px;
        }

        /* ── Remove TODOS os botões de copiar em qualquer elemento ── */
        button[title="Copy to clipboard"],
        [data-testid="stCopyButton"],
        [data-testid="stMetricValue"] button,
        [data-testid="InputInstructions"],
        .stCodeBlock button,
        .stTextInput button,
        .stTextArea button,
        [class*="copyButton"],
        [class*="copy-button"],
        [class*="CopyButton"],
        div[class*="stCode"] button,
        div[class*="toolbar"] button[kind="secondary"],
        div[data-testid="stToolbar"] button,
        section[data-testid="stSidebar"] button[title="Copy to clipboard"] {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
            pointer-events: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown("## 🌱 EcoLogic Systems Tecnologia Ltda.")
st.markdown("*Tecnologia pensada para pessoas e para o planeta*")
st.divider()

# ── Função de envio de e-mail ──────────────────────────────────────────────────
def enviar_email(nome, email_remetente, assunto, mensagem):
    try:
        EMAIL_CONTA   = st.secrets["EMAIL"]
        SENHA         = st.secrets["SENHA_EMAIL"]
        EMAIL_DESTINO = "guilhermecavalcantelopes99@gmail.com"

        msg = MIMEMultipart()
        msg["From"]    = EMAIL_CONTA
        msg["To"]      = EMAIL_DESTINO
        msg["Subject"] = f"[{assunto}] Contato de {nome} pelo site"

        agora = datetime.now().strftime("%d/%m/%Y às %H:%M")

        corpo = f"""
Olá,

{nome} entrou em contato pelo site da EcoLogic Systems e aguarda um retorno.

    Assunto: {assunto}
    E-mail para resposta: {email_remetente}
    Mensagem: {mensagem}

Mensagem recebida em {agora}.

Atenciosamente,
EcoLogic Systems
        """

        msg.attach(MIMEText(corpo, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as servidor:
            servidor.starttls()
            servidor.login(EMAIL_CONTA, SENHA)
            servidor.sendmail(EMAIL_CONTA, EMAIL_DESTINO, msg.as_string())

        return True, None

    except Exception as e:
        return False, str(e)

# ── Abas ──────────────────────────────────────────────────────────────────────
aba1, aba2, aba3, aba4, aba5 = st.tabs([
    "Início", "Nossa Empresa", "Serviços", "Contato", "📊 Estatísticas"
])

# ── ABA 1: INÍCIO ──────────────────────────────────────────────────────────────
with aba1:
    st.title("Bem-vindo à EcoLogic Systems")
    st.write(
        "Somos uma empresa que acredita que tecnologia e responsabilidade "
        "ambiental andam juntas. Estamos aqui para ajudar você."
    )
    st.divider()

    col1, col2, col3 = st.columns(3)
    col1.metric("Foco",        "Sustentabilidade")
    col2.metric("Tecnologia",  "Responsável")
    col3.metric("Localização", "Santo André - SP")

    st.divider()

    st.subheader("Por que trabalhar com a EcoLogic?")
    col_a, col_b, col_c = st.columns(3)

    with col_a:
        st.success(
            "**Compromisso ambiental**\n\n"
            "Cada projeto leva em conta o impacto no meio ambiente."
        )
    with col_b:
        st.info(
            "**Soluções que funcionam**\n\n"
            "Tecnologia moderna, sem complicar o que pode ser simples."
        )
    with col_c:
        st.warning(
            "**Atendimento próximo**\n\n"
            "Nossa equipe está disponível para te ouvir de verdade."
        )

# ── ABA 2: NOSSA EMPRESA ───────────────────────────────────────────────────────
with aba2:
    st.title("Conheça a Nossa Empresa")
    st.divider()

    st.subheader("Quem somos")
    st.write(
        "A EcoLogic Systems nasceu da vontade de unir tecnologia e "
        "responsabilidade. Acreditamos que é possível construir um negócio "
        "sólido sem abrir mão do cuidado com o meio ambiente e com as pessoas."
    )
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Nossa Missão")
        st.write(
            "Desenvolver soluções que gerem valor real para nossos clientes "
            "e contribuam para um futuro mais sustentável."
        )

        st.subheader("Nossa Visão")
        st.write(
            "Ser reconhecida como uma empresa de tecnologia que as pessoas "
            "confiam pela forma como trabalhamos."
        )

    with col2:
        st.subheader("Nossos Valores")
        valores = [
            "Sustentabilidade",
            "Inovação com propósito",
            "Compromisso com o cliente",
            "Responsabilidade ambiental"
        ]
        for valor in valores:
            st.write(f"• {valor}")

# ── ABA 3: SERVIÇOS ────────────────────────────────────────────────────────────
with aba3:
    st.title("O que oferecemos")
    st.write("Serviços acessíveis e diretos ao ponto.")
    st.divider()

    servicos = [
        ("Criação de Sites",        "Sites simples e bem feitos para apresentar sua empresa na internet."),
        ("Suporte Técnico",         "Ajuda quando algo não funciona, seja num equipamento ou sistema."),
        ("Segurança da Informação", "Orientamos sobre como proteger os dados da sua empresa."),
        ("Uso Consciente",          "Como usar a internet e dispositivos de forma segura e responsável."),
        ("Descarte Eletrônico",     "Indicamos onde descartar equipamentos sem prejudicar o meio ambiente."),
    ]

    col1, col2 = st.columns(2)

    for i, (titulo, descricao) in enumerate(servicos):
        if i % 2 == 0:
            with col1:
                st.info(f"**{titulo}**\n\n{descricao}")
        else:
            with col2:
                st.info(f"**{titulo}**\n\n{descricao}")

# ── ABA 4: CONTATO ─────────────────────────────────────────────────────────────
with aba4:
    st.title("Entre em Contato")
    st.write("Preencha o formulário e entraremos em contato em breve.")
    st.divider()

    col_form, col_info = st.columns(2)

    with col_form:
        nome     = st.text_input("Seu nome")
        email    = st.text_input("Seu e-mail")
        assunto  = st.selectbox("Assunto", [
            "Dúvida",
            "Orçamento",
            "Parceria",
            "Elogio",
            "Outro"
        ])
        mensagem = st.text_area("Mensagem", height=150)

        if st.button("Enviar mensagem"):

            if nome == "" or email == "" or mensagem == "":
                st.warning("Por favor, preencha todos os campos.")

            elif "@" not in email:
                st.warning("O e-mail informado parece inválido.")

            else:
                agora = datetime.now().strftime("%d/%m/%Y às %H:%M")

                # ── Salva em CSV ──────────────────────────────────────────────
                arquivo_existe = os.path.exists("mensagens.csv")

                with open("mensagens.csv", "a", newline="", encoding="utf-8") as arquivo:
                    writer = csv.writer(arquivo)
                    if not arquivo_existe:
                        writer.writerow(["Nome", "Email", "Assunto", "Mensagem", "Data"])
                    writer.writerow([nome, email, assunto, mensagem, agora])

                # ── Envia e-mail ──────────────────────────────────────────────
                with st.spinner("Enviando sua mensagem..."):
                    sucesso, erro = enviar_email(nome, email, assunto, mensagem)

                if sucesso:
                    st.success(
                        f"Obrigado, {nome}! Recebemos sua mensagem e "
                        f"entraremos em contato em breve."
                    )
                    st.balloons()
                else:
                    st.error(
                        "Não foi possível enviar agora. Entre em contato "
                        "diretamente pelo e-mail guilhermecavalcantelopes99@gmail.com"
                    )
                    st.caption(f"Detalhe técnico: {erro}")

    with col_info:
        st.subheader("Informações de Contato")
        st.write("guilhermecavalcantelopes99@gmail.com")
        st.write("Santo André - SP")
        st.divider()

        st.subheader("Horário de Atendimento")
        st.write("Segunda a Sexta: 08h às 18h")
        st.write("Sábado: 08h às 12h")
        st.divider()

        st.subheader("Nossa Localização")
        localizacao = pd.DataFrame({
            "lat": [-23.6647],
            "lon": [-46.5388]
        })
        st.map(localizacao)

# ── ABA 5: ESTATÍSTICAS ────────────────────────────────────────────────────────
with aba5:
    st.title("📊 Estatísticas de Contato")
    st.write("Análise das mensagens recebidas pelo site.")
    st.divider()

    if not os.path.exists("mensagens.csv"):
        st.info("Nenhuma mensagem recebida ainda. As estatísticas aparecerão aqui assim que houver contatos.")

    else:
        df = pd.read_csv("mensagens.csv")

        # ── Card total de mensagens ───────────────────────────────────────────
        st.metric("📬 Total de mensagens recebidas", len(df))
        st.divider()

        # ── 1: Tabela de Frequências ─────────────────────────────────────────
        st.subheader("📋 Tabela de Frequências por Assunto")
        st.caption("Frequência Absoluta (fi), Relativa (fri) e Percentual (%) — Aula 1")

        freq = df["Assunto"].value_counts().reset_index()
        freq.columns = ["Assunto", "fi (Freq. Absoluta)"]
        freq["fri (Freq. Relativa)"] = (
            freq["fi (Freq. Absoluta)"] / len(df)
        ).round(4)
        freq["% (Freq. Percentual)"] = (
            freq["fri (Freq. Relativa)"] * 100
        ).round(2)

        freq = freq[["Assunto", "fi (Freq. Absoluta)", "fri (Freq. Relativa)", "% (Freq. Percentual)"]]

        st.dataframe(freq, use_container_width=True)
        st.divider()

        # ── 2: Moda ───────────────────────────────────────────────────────────
        st.subheader("🏆 Moda")
        st.caption("O assunto mais enviado — Aula 3")

        moda          = df["Assunto"].mode()[0]
        contagem_moda = df["Assunto"].value_counts()[moda]

        col1, col2 = st.columns(2)
        col1.metric("Assunto mais frequente (Moda)", moda)
        col2.metric("Quantidade de vezes", contagem_moda)
        st.divider()

        # ── 4: Média e Mediana do horário ─────────────────────────────────────
        st.subheader("🕐 Média e Mediana do Horário de Contato")
        st.caption("Hora média e mediana dos contatos recebidos — Aula 3")

        df["Data_dt"] = pd.to_datetime(
            df["Data"], format="%d/%m/%Y às %H:%M", errors="coerce"
        )
        df["Hora"] = df["Data_dt"].dt.hour

        media_hora   = df["Hora"].mean()
        mediana_hora = df["Hora"].median()

        col3, col4 = st.columns(2)
        col3.metric("Hora média de contato", f"{media_hora:.1f}h")
        col4.metric("Mediana do horário",    f"{mediana_hora:.0f}h")

        hora_freq = df["Hora"].value_counts().sort_index().reset_index()
        hora_freq.columns = ["Hora do dia", "Mensagens recebidas"]
        st.dataframe(hora_freq, use_container_width=True)
        st.divider()

        # ── 5: Gráfico de Série Específica ────────────────────────────────────
        st.subheader("📊 Série Específica: Mensagens por Assunto")
        st.caption("Varia o fato (assunto), permanece o local e época — Aula 2")

        serie_assunto = df["Assunto"].value_counts()
        st.bar_chart(serie_assunto)

# ── Rodapé ─────────────────────────────────────────────────────────────────────
st.markdown("""
    <div class="rodape">
        EcoLogic Systems Tecnologia Ltda. | Santo André - SP | © 2026
    </div>
""", unsafe_allow_html=True)
