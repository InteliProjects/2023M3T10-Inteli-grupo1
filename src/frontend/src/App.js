import { useState, useRef } from "react";

import Header from "./Header";
import HomeMain from "./HomeMain";
import AboutUs from "./AboutUs";
import Footer from "./Footer";
import UseGuide from "./UseGuide";
import WalletsByType from "./WalletsByType";

export default function App() {
    const walletsRef = useRef(null);
    const wallets2Ref = useRef(null);
    const aboutUsRef = useRef(null);
    const ourTeamRef = useRef(null);

    const [activePage, setActivePage] = useState(0);

    const [funds, setFunds] = useState({});
    const [historicFunds, setHistoricFunds] = useState({});

    const [isLoading, setIsLoading] = useState(false);

    function scrollToWallets() {
        if (walletsRef.current) {
            walletsRef.current.scrollIntoView({ behavior: "smooth" });
        }
    }

    function scrollToAboutUs() {
        if (aboutUsRef.current) {
            aboutUsRef.current.scrollIntoView({ behavior: "smooth" });
        }
    }

    function scrollToOurTeam() {
        if (ourTeamRef.current) {
            ourTeamRef.current.scrollIntoView({ behavior: "smooth" });
        }
    }

    function renderPage() {
        switch (activePage) {
            case 1:
                return (
                    <>
                        <UseGuide
                            setFunds={setFunds}
                            setHistoricFunds={setHistoricFunds}
                            isLoading={isLoading}
                            setIsLoading={setIsLoading}
                            scrollToWallets={scrollToWallets}
                        />
                        <WalletsByType
                            title="Novos fundos"
                            funds={funds}
                            isLoading={isLoading}
                            walletsRef={walletsRef}
                        />
                        <WalletsByType
                            title="Histórico"
                            funds={historicFunds}
                            isLoading={isLoading}
                            walletsRef={wallets2Ref}
                        />
                    </>
                );
            default:
                return (
                    <>
                        <HomeMain setActivePage={setActivePage} />
                        <AboutUs
                            aboutUsRef={aboutUsRef}
                            ourTeamRef={ourTeamRef}
                        />
                    </>
                );
        }
    }

    return (
        <>
            <Header
                setActivePage={setActivePage}
                scrollToAboutUs={scrollToAboutUs}
                scrollToOurTeam={scrollToOurTeam}
            />
            {renderPage()}
            <Footer
                setActivePage={setActivePage}
                scrollToAboutUs={scrollToAboutUs}
                scrollToOurTeam={scrollToOurTeam}
            />
        </>
    );
}
