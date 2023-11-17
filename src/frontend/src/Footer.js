import styled from "styled-components";
import logo from "./assets/logo_fidcas.png";
import cvm from "./assets/cvm.png";
import inteli from "./assets/inteli.png";

export default function Footer({
    setActivePage,
    scrollToAboutUs,
    scrollToOurTeam,
}) {
    return (
        <Container>
            <div>
                <p
                    onClick={() => {
                        setActivePage(0);
                        setTimeout(() => {
                            window.scrollTo(0, 0);
                        }, 100);
                    }}
                >
                    Home
                </p>
                <p
                    onClick={() => {
                        setActivePage(0);
                        setTimeout(() => {
                            scrollToAboutUs();
                        }, 100);
                    }}
                >
                    Sobre
                </p>
                <p
                    onClick={() => {
                        setActivePage(1);
                        setTimeout(() => {
                            window.scrollTo(0, 0);
                        }, 100);
                    }}
                >
                    Guia de utilização
                </p>
                <div>
                    <img src={logo} alt="logo fidcas" />
                    <h1
                        onClick={() => {
                            setActivePage(0);
                            setTimeout(() => {
                                window.scrollTo(0, 0);
                            }, 100);
                        }}
                    >
                        PREDICAS
                    </h1>
                </div>
                <p
                    onClick={() => {
                        setActivePage(0);
                        setTimeout(() => {
                            scrollToOurTeam();
                        }, 100);
                    }}
                >
                    Nossa equipe
                </p>
                <p>
                    <a
                        href="https://fnet.bmfbovespa.com.br/fnet/publico/pesquisarGerenciadorDocumentosCVM?paginaCertificados=false&tipo%20Fundo=1&administrador=&cnpjFundo=11026627000138&idCategoriaDocumento=0&idTipoDocumento=0&idEspecie%20%20Documento=0&situacao=&cnpj=&dataReferencia=&dataInicial=&dataFinal=&idModalidade=&palavraChave="
                        target="_blank"
                        rel="noopener noreferrer"
                    >
                        Baixe o informe
                    </a>
                </p>
            </div>
            <Divider />
            <div>
                <h1>Parceiros</h1>
                <div>
                    <img src={cvm} alt="logo cvm" />
                    <div style={{ display: "flex", alignItems: "center" }}>
                        <img src={logo} alt="logo fidcas" />
                        <h1>FIDCAS</h1>
                    </div>
                    <img src={inteli} alt="logo inteli" />
                </div>
            </div>
        </Container>
    );
}

const Container = styled.div`
    width: 100%;
    min-height: 60vh;

    background-color: #f2f2f2;
    padding: 70px 15%;

    h1 {
        font-size: 24px;
        font-style: normal;
        font-weight: 700;
        line-height: normal;
        color: #000;

        cursor: pointer;
    }

    p {
        color: #000;
        font-size: 14px;
        font-style: normal;
        font-weight: 700;

        cursor: pointer;
    }

    > div:first-child {
        display: flex;
        justify-content: space-between;
        align-items: center;

        padding: 30px 10%;

        > div {
            display: flex;
            align-items: center;
        }
    }

    > div:last-child {
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;

        margin-top: 30px;

        > div {
            width: 45%;
            display: flex;
            justify-content: space-between;

            > img {
                width: 100px;
                height: 100px;

                object-fit: contain;
            }
        }
    }

    a {
        color: #000;
        text-decoration: none;
    }
`;

const Divider = styled.div`
    width: 100%;
    height: 2px;

    background-color: #000;
`;
