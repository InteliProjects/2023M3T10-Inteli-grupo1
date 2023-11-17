import { useState } from "react";
import Accordion from "react-bootstrap/Accordion";
import Carousel from "react-bootstrap/Carousel";
import styled from "styled-components";
import { Line } from "react-chartjs-2";
import {
    Chart,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    LineController,
} from "chart.js";

Chart.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    LineController
);

export default function RenderFidcs({ title, fidcs }) {
    const [activeIndex, setActiveIndex] = useState(0);

    function handleSelect(selectedIndex, e) {
        setActiveIndex(selectedIndex);
    }

    function renderFidcs() {
        return fidcs ? (
            fidcs.map((fidc, index) => {
                fidc.Dados.datasets[0].borderColor = "rgb(255, 99, 132)"; //inad
                fidc.Dados.datasets[1].borderColor = "rgb(54, 162, 235)"; //prov
                fidc.Dados.datasets[2].borderColor = "rgb(255, 159, 64)"; //subst
                fidc.Dados.datasets[3].borderColor = "rgb(153, 102, 255)"; //recomp

                const data = {
                    labels: fidc.Dados.labels,
                    datasets: [fidc.Dados.datasets[0], fidc.Dados.datasets[1]],
                };

                const data2 = {
                    labels: fidc.Dados.labels,
                    datasets: [fidc.Dados.datasets[2], fidc.Dados.datasets[3]],
                };

                return (
                    <Carousel.Item key={index}>
                        <h1>
                            <span>Nome do fundo:</span> {fidc.Nome}
                        </h1>
                        <ChartHolder>
                            <Charts>
                                <div>
                                    <h1>
                                        <ColoredCircle backgroundColor="rgb(255, 99, 132)" />
                                        Inadimplência
                                    </h1>
                                    <h1>
                                        <ColoredCircle backgroundColor="rgb(54, 162, 235)" />
                                        Provisão
                                    </h1>
                                </div>
                                <Line data={data} />
                            </Charts>
                            <Charts>
                                <div>
                                    <h1>
                                        <ColoredCircle backgroundColor="rgb(255, 159, 64)" />
                                        Substituição
                                    </h1>
                                    <h1>
                                        <ColoredCircle backgroundColor="rgb(153, 102, 255)" />
                                        Recompra
                                    </h1>
                                </div>
                                <Line data={data2} />
                            </Charts>
                        </ChartHolder>
                        <FundData>
                            <h1>
                                <span>Administradora:</span> {fidc.CNPJ}
                            </h1>
                            <button>
                                <a
                                    href={`https://fnet.bmfbovespa.com.br/fnet/publico/pesquisarGerenciadorDocumentosCVM?paginaCertificados=false&tipo%20Fundo=1&administrador=&cnpjFundo=&idCategoriaDocumento=0&idTipoDocumento=0&idEspecie%20%20Documento=0&situacao=&cnpj=&dataReferencia=&dataInicial=&dataFinal=&idModalidade=&palavraChave=`}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                >
                                    Buscar fundo
                                </a>
                            </button>
                        </FundData>
                    </Carousel.Item>
                );
            })
        ) : (
            <> </>
        );
    }

    return (
        <Container>
            <Accordion style={{ width: "70%" }}>
                <Accordion.Item eventKey="0">
                    <Accordion.Header>{title}</Accordion.Header>
                    <Accordion.Body style={{ backgroundColor: "#f2f2f2" }}>
                        <StyledCarousel
                            indicators={false}
                            activeIndex={activeIndex}
                            onSelect={handleSelect}
                        >
                            {renderFidcs()}
                        </StyledCarousel>
                    </Accordion.Body>
                </Accordion.Item>
            </Accordion>
        </Container>
    );
}

const Container = styled.div`
    display: flex;
    justify-content: center;

    margin-bottom: 30px;

    button {
        background-color: #f2f2f2;
        border: none;
    }
`;

const ChartHolder = styled.div`
    width: 100%;
    height: 300px;

    display: flex;
    justify-content: space-evenly;
    align-items: center;
`;

const Charts = styled.div`
    width: 100%;
    height: 300px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: space-between;

    > div:first-child {
        width: 100%;
        height: 50px;

        display: flex;
        justify-content: space-evenly;
        align-items: center;
    }

    h1 {
        display: flex;
    }
`;

const ColoredCircle = styled.div`
    width: 15px;
    height: 15px;

    margin-right: 10px;

    border-radius: 50%;
    background-color: ${(props) => props.backgroundColor};
`;

const StyledCarousel = styled(Carousel)`
    .carousel-control-prev-icon,
    .carousel-control-next-icon {
        background-color: #000; // Set the color of your choice here.
    }

    h1 {
        color: #000;
        font-size: 20px;
        font-style: normal;
        font-weight: 400;
    }

    span {
        color: #000;

        font-size: 20px;
        font-style: normal;
        font-weight: 555;
        line-height: 140.625%;
    }

    button {
        width: 140px;
        height: 35px;

        border-radius: 5px;
        border: 1px solid #fff;
        background-color: #000;

        font-size: 16px;
        font-weight: 400;
        margin: 0 20px;

        cursor: pointer;
    }

    a {
        text-decoration: none;
        color: #fff;
    }
`;

const FundData = styled.div`
    width: 100%;
    height: 50px;

    margin-top: 20px;

    display: flex;
    justify-content: center;
    align-items: center;
`;
