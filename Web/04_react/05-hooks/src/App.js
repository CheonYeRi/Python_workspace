
import './App.css';
import CssModule from './components/CssModule';
import Faq from './components/Faq';
import StyledComponent from './components/StyledComponent';
import UseMemoEx from './components/UseMemoEx1';

function App() {
  return (
    <div className="App">
      {/* <h1>실행</h1>
      <UseMemoEx />

      <hr />
      <Faq /> */}

      <hr />
      <CssModule />

      {/* Styled Component */}
      <hr />
      <h2> Styled-component</h2>
      <StyledComponent />
    </div>
  );
}

export default App;
