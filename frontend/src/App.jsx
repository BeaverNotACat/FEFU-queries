import {
  Route,
  Routes,
  BrowserRouter as Router,
} from "react-router-dom";

import Login from './routes/Login'
import Forms from './routes/Forms'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/forms/:id" element={<Forms />} />
        <Route path="/add_form_populations" />
      </Routes>
    </Router>
  );
}

export default App;
