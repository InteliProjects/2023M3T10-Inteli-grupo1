import styled from "styled-components";
import logo from "./assets/logo_fidcas.png";

export default function Header({
    setActivePage,
    scrollToAboutUs,
    scrollToOurTeam,
}) {
    return (
        <Container>
            <div>
                <img
                    src={logo}
                    alt="logo fidcas"
                    onClick={() => setActivePage(0)}
                />
                <h1 onClick={() => setActivePage(0)}>FIDCAS</h1>
            </div>
            <div>
                <h2 onClick={() => setActivePage(0)}>Home</h2>
                <h2
                    onClick={() => {
                        setActivePage(0);
                        setTimeout(() => {
                            scrollToAboutUs();
                        }, 100);
                    }}
                >
                    Sobre
                </h2>
                <h2 onClick={() => setActivePage(1)}>Guia de utilização</h2>
                <h2
                    onClick={() => {
                        setActivePage(0);
                        setTimeout(() => {
                            scrollToOurTeam();
                        }, 100);
                    }}
                >
                    Nossa equipe
                </h2>
                <button>
                    <a
                        href="https://fnet.bmfbovespa.com.br/fnet/publico/pesquisarGerenciadorDocumentosCVM?paginaCertificados=false&tipo%20Fundo=1&administrador=&cnpjFundo=11026627000138&idCategoriaDocumento=0&idTipoDocumento=0&idEspecie%20%20Documento=0&situacao=&cnpj=&dataReferencia=&dataInicial=&dataFinal=&idModalidade=&palavraChave="
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        Baixe o informe
                    </a>
                </button>
            </div>
        </Container>
    );
}

const Container = styled.div`
    width: 100%;
    height: 64px;

    padding: 0 10px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    > div {
        display: flex;
        align-items: center;

        width: 50%;
    }

    > div:first-child {
        justify-content: flex-start;
    }

    > div:last-child {
        justify-content: flex-end;
    }

    h1 {
        font-size: 24px;
        font-weight: 700;
        margin-left: 20px;

        cursor: pointer;
    }

    h2 {
        font-size: 16px;
        font-weight: 400;
        margin-left: 20px;

        cursor: pointer;

        &:hover {
            text-decoration: underline;
            text-decoration-color: #000;
            text-decoration-thickness: 2px;
            text-underline-offset: 5px;
        }
    }

    button {
        width: 140px;
        height: 35px;

        border-radius: 5px;
        border: 1px solid #000;
        background-color: #fff;

        color: #000;
        font-size: 16px;
        font-weight: 400;
        margin: 0 20px;

        cursor: pointer;
    }

    a {
        text-decoration: none;
        color: #000;
    }
`;
