import { useState } from 'react';
import Result from './Result';
import Select from './Select';
import Input from './ExAll/EInput';

function ExAll() {
  // 상태
    const [data, setData] = useState({
        fruit: 'apple',
        background: 'black',
        color: 'black',
        content: 'text',
    });

    return (
        <>
        <div
            style={{
            display: 'flex',
            justifyContent: 'center',
            marginTop: '10px',
            }}
        >
            <Select setData={setData} />
        </div>
        <div
            style={{
            display: 'flex',
            justifyContent: 'center',
            marginTop: '10px',
            }}
        >
            <Input setData={setData} />
        </div>
        <div
            style={{
            display: 'flex',
            justifyContent: 'center',
            marginTop: '10px',
            }}
        >
            <Result data={data} />
        </div>
        </>
    );
}

export default ExAll;