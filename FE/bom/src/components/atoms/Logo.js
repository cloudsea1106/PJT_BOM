import React from "react";

import { Link } from "react-router-dom";

import symbol from "assets/bom_symbol_50.png";

function Logo({ size = "l", logoClassName }) {
  return (
    <Link to="/">
      {size === "s" && (
        <div className={`flex items-center ${logoClassName}`}>
          <img src={symbol} alt="BOM 심볼" className="inline mr-2 w-[30px]" />
          <span className="font-righteous text-main text-xl tracking-wider">
            BOM
          </span>
          {/* </Link> */}
        </div>
      )}
      {size === "l" && (
        <div className={`flex items-center ${logoClassName}`}>
          {/* <Link to="/"> */}
          <img src={symbol} alt="BOM 심볼" className="inline mr-2 w-[35px]" />
          <span className="font-righteous text-main text-2xl tracking-wider">
            BOM
          </span>
        </div>
      )}
    </Link>
  );
}

export default Logo;
