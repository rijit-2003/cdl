import React from 'react';
import data from '../assets/scientists.json';
import TimelineItem from './TimelineItem';
import './styles/Timeline.css';

function Timeline() {
  return (
    <div className="timeline-container">
      {data.map((sci, index) => (
        <TimelineItem
          key={sci.id}
          id={sci.id}
          name={sci.name}
          image={sci.image}
          side={index % 2 === 0 ? 'left' : 'right'}
        />
      ))}
    </div>
  );
}

export default Timeline;
