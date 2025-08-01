import React from 'react';
import './styles/Timeline.css';
import { Link } from 'react-router-dom';

function TimelineItem({ side, name, period, image, id }) {
  return (
    <div className={`timeline-item ${side}`}>
      {side === 'left' ? (
        <>
          <div className="timeline-content content-left">
            <Link to={`/scientist/${id}`}>
              <img src={`/images/${image}`} alt={name} className="timeline-img" />
              <div className="timeline-name">{name}</div>
            </Link>
          </div>
          <div className="timeline-period">{period}</div>
        </>
      ) : (
        <>
          <div className="timeline-period">{period}</div>
          <div className="timeline-content content-right">
            <Link to={`/scientist/${id}`}>
              <img src={`/images/${image}`} alt={name} className="timeline-img" />
              <div className="timeline-name">{name}</div>
            </Link>
          </div>
        </>
      )}
    </div>
  );
}

export default TimelineItem;
