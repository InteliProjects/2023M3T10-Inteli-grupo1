import styled from "styled-components";
import axios from "axios";
import { Oval } from "react-loader-spinner";

export default function UserGuide({
    setFunds,
    setHistoricFunds,
    setIsLoading,
    isLoading,
    scrollToWallets,
}) {
    const uploadFile = async (event) => {
        setIsLoading(true);
        const file = event.target.files[0];
        if (!file) return;
        const formData = new FormData();
        formData.append("file", file);
        try {
            const response = await axios.post(
                "http://localhost:5000/api",
                formData,
                {
                    headers: { "Content-Type": "multipart/form-data" },
                }
            );

            setFunds({ ...JSON.parse(response.data.result).outliers_novos });
            setHistoricFunds({
                ...JSON.parse(response.data.result).outliers_historicos,
            });
            setIsLoading(false);
            scrollToWallets();
        } catch (error) {
            console.error("Error uploading file:", error);
            setIsLoading(false);
        }
    };

    return (
        <Container>
            <div>
                <h1>Guia de utilização</h1>
                <p>
                    Para utilizar o modelo e realizar a análise dos fundos, é
                    preciso fazer o upload de um arquivo .csv contendo os dados
                    dos informes mensais. São dois passos simples:
                </p>
                <Topic>
                    <div>1</div>
                    <div>
                        <h3>Upload</h3>
                        <h4>
                            Efetuar o upload do aquivo .csv e aguardar a análise
                            do modelo.
                        </h4>
                    </div>
                </Topic>
                <Topic>
                    <div>2</div>
                    <div>
                        <h3>Visualização</h3>
                        <h4>
                            Com a finalização dos processos, são dispostos
                            gráficos e a identificação referentes aos fundos
                            anômalos logo abaixo.
                        </h4>
                    </div>
                </Topic>
            </div>
            <div>
                <WhiteBox>
                    {isLoading ? (
                        <Oval color="#30947c" />
                    ) : (
                        <label htmlFor="fileUpload">Faça Upload</label>
                    )}
                    <input
                        id="fileUpload"
                        type="file"
                        accept=".csv"
                        onChange={uploadFile}
                    />
                </WhiteBox>
            </div>
        </Container>
    );
}

const Container = styled.div`
    width: 100%;
    min-height: 70vh;

    background-color: #f2f2f2;
    padding-top: 100px;

    display: flex;

    > div {
        width: 50%;

        padding: 0 10%;
    }

    h1 {
        color: #000;
        text-align: left;

        font-size: 48px;
        font-style: normal;
        font-weight: 500;
        line-height: 82.031%; /* 39.375px */

        margin-bottom: 60px;
    }

    p {
        color: #9090a7;
        text-align: left;
        font-size: 16px;
        font-style: normal;
        font-weight: 400;
        line-height: 28px; /* 175% */

        margin-bottom: 40px;
    }

    > div:last-child {
        display: flex;
        align-items: center;
        justify-content: center;
    }
`;

const Topic = styled.div`
    display: flex;
    align-items: center;
    justify-content: space-between;

    margin-bottom: 40px;

    > div:first-child {
        width: 50px;
        height: 50px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 12px;
        background: #fff;

        color: #30947c;
        text-align: center;
        font-style: normal;
        font-weight: 500;
        font-size: 35px;
    }

    > div:last-child {
        width: 78%;
    }

    h3 {
        color: #060640;

        font-size: 20px;
        font-style: normal;
        font-weight: 500;
        line-height: 28px; /* 140% */
    }

    h4 {
        color: #9090a7;

        font-size: 16px;
        font-style: normal;
        font-weight: 400;
        line-height: 28px; /* 175% */
    }
`;

const WhiteBox = styled.div`
    width: 100%;
    height: 60%;

    background: #fff;
    border-radius: 12px;

    display: flex;
    align-items: center;
    justify-content: center;

    > label {
        display: flex;
        align-items: center;
        justify-content: center;

        width: 50%;
        height: 50px;
        background-color: #30947c;
        border-radius: 12px;
        border: none;

        cursor: pointer;

        color: #fff;
        font-size: 20px;
    }

    > input {
        display: none;
    }
`;
