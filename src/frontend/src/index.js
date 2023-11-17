import ReactDOM from "react-dom/client";
import App from "./App";

import "./styles/reset.css";
import "./styles/globalStyles.css";
import "bootstrap/dist/css/bootstrap.min.css";

const root = document.getElementById("root");
const rootContainer = ReactDOM.createRoot(root);

rootContainer.render(<App />);
