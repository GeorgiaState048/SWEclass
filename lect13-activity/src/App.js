import logo from './logo.svg';
import './App.css';
import {TVShow} from './TVShow';


function App() {
  return (
    <div className="App">
      <ol>
        <TVShow name="Daredevil"/>
        <li>Stranger Things</li>
        <TVShow name="Euphoria"/>
      </ol>
    </div>
  );
}

export default App;
