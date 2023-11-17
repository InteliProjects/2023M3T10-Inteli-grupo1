import styled from "styled-components";
import { Oval } from "react-loader-spinner";

import RenderFidcs from "./RenderFidcs";

export default function WalletsByType({ title, funds, isLoading, walletsRef }) {
    function returnPage() {
        if (!isLoading && funds["Serviços"]) {
            return (
                <>
                    <h1>{title}</h1>
                    <RenderFidcs title={"Serviços"} fidcs={funds["Serviços"]} />
                    <RenderFidcs
                        title={"Industrial"}
                        fidcs={funds["Industrial"]}
                    />
                    <RenderFidcs title={"Cartão"} fidcs={funds["Cartão"]} />
                    <RenderFidcs
                        title={"Agronegócio"}
                        fidcs={funds["Agronegócio"]}
                    />
                    <RenderFidcs
                        title={"Factoring"}
                        fidcs={funds["Factoring"]}
                    />
                    <RenderFidcs
                        title={"Imobiliário"}
                        fidcs={funds["Imobiliário"]}
                    />
                    <RenderFidcs
                        title={"Comercial"}
                        fidcs={funds["Comercial"]}
                    />
                </>
            );
        }

        if (!isLoading && !funds["Serviços"]) {
            return <NoCSVSent>Aguardando envio do CSV...</NoCSVSent>;
        }
    }

    return <Container ref={walletsRef}>{returnPage()}</Container>;
}

const Container = styled.div`
    width: 100%;
    min-height: 70vh;

    padding: 10px 0;

    text-align: center;

    h1 {
        margin: 30px 0;
    }
`;

const NoCSVSent = styled.div`
    width: 100%;
    height: 100%;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 20px;
    font-style: italic;
    font-weight: 700;
    color: #000;
`;
