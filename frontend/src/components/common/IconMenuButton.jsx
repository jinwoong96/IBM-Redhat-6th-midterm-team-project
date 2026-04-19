import React from 'react';

const IconMenuButton = ({content, onClick}) => {
    return (
        <button onClick={()=>{onClick()}}>
            {content}
        </button>
    );
};

export default IconMenuButton;