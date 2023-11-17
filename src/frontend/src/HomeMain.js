import styled from "styled-components";
import logo from "./assets/logo_fidcas.png";

export default function HomeMain({ setActivePage }) {
    return (
        <Container>
            <div>
                <ContentHolder>
                    <h1>
                        Dicas de Previsão<br></br>e Provisão
                    </h1>
                    <h2>
                        Bem vindo ao site do grupo FIDCAS! Aqui, você pode
                        utilizar o modelo de análise de FIDCs com comportamentos
                        anômalos para visualizar, em tempo real, os fundos de
                        investimento em direitos creditórios que precisam de
                        mais atenção. Basta clicar no botão abaixo!
                    </h2>
                    <button onClick={() => setActivePage(1)}>
                        Use o modelo
                    </button>
                </ContentHolder>
            </div>
            <div>
                <BiggerBlock>
                    <SmallerBlock>
                        <img src={logo} alt="logo fidcas" />
                    </SmallerBlock>
                </BiggerBlock>
            </div>
        </Container>
    );
}

const Container = styled.div`
    width: 100%;
    height: 75vh;
    min-height: 75vh;

    display: flex;
    align-items: center;
    background-color: rgba(242, 242, 242, 0.8);

    > div {
        width: 50%;
        height: 100%;
    }

    > div:first-child {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    h1 {
        font-size: 40px;
        font-style: normal;
        font-weight: 500;

        margin-bottom: 60px;
    }

    h2 {
        font-size: 20px;
        font-style: normal;
        font-weight: 400;

        margin-bottom: 60px;
    }

    button {
        width: 160px;
        height: 50px;

        border-radius: 5px;
        background: #000;
        font-size: 18px;
        font-style: normal;
        font-weight: 400;
        color: #fff;

        cursor: pointer;
    }

    > div:last-child {
        display: flex;
        justify-content: flex-end;
        align-items: center;
    }
`;

const ContentHolder = styled.div`
    width: 60%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
`;

const BiggerBlock = styled.div`
    width: 90%;
    height: 70%;
    border-radius: 20px 0px 0px 20px;
    background: rgba(255, 214, 0, 0.58);

    position: relative;
`;

const SmallerBlock = styled.div`
    width: 50%;
    height: 45%;

    border-radius: 20px;
    background: rgba(255, 192, 0, 0.59);

    display: flex;
    justify-content: center;
    align-items: center;

    position: absolute;
    top: 15%;
    left: -5%;

    img {
        width: 80px;
        height: 80px;

        object-fit: cover;
    }
`;
