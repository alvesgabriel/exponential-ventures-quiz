import React from "react";

import "./App.css";
import { AuthProvider } from "./components/Context/AuthContext";
import Routes from "./pages/Routes";

class App extends React.Component {
  render() {
    return (
      <AuthProvider>
        <Routes />
      </AuthProvider>
    );
  }
}

export default App;
