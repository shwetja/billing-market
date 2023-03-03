import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import Add from './Components/stocks_components/Pages/User/Add';
import Show from './Components/stocks_components/Pages/User/Show';
import Home from './Components/stocks_components/Pages/Home';
import NavBar from './Components/stocks_components/Layout/NavBar';
import Update from './Components/stocks_components/Pages/User/Update';
import Delete from './Components/stocks_components/Pages/User/Delete';



function App() {
  return (
    <>
      
      <BrowserRouter>
      <NavBar/>
        <Routes>
              
              <Route exact path="/home" element={<Home />}/>
              <Route exact path="/user/add" element={<Add />}/>
              <Route exact path="/user/show" element={<Show />}/>
              <Route exact path="/user/update/:userId" element={<Update />}/>
              <Route exact path="/user/delete/:userId" element={<Delete/>}/>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
