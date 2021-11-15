import argparse
from collections import defaultdict
import jsonlines
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--extracted-relations-file', type=str, required=False, default="/Users/vijay/Downloads/extracted_drugs_distant_supervision_large_multi_sentences_per_doc.jsonl")
parser.add_argument('--min-frequency', type=int, required=False, default=20)
parser.add_argument('--label-threshold', type=int, required=False, default=0.6)


def return_relations_meeting_frequency(relation_counts, min_freq):
    relations = []
    for r, freq in relation_counts.items():
        if freq >= min_freq:
            relations.append(list(r))
    return relations

if __name__ == "__main__":
    args = parser.parse_args()
    relation_labels = {"COMB": defaultdict(int), "POS": defaultdict(int), "NEG": defaultdict(int), "NO_COMB": defaultdict(int)}
    for row in tqdm(jsonlines.open(args.extracted_relations_file)):
        drug_relation = tuple(row["drug_combination"])
        pos_prob = row["relation_probabilities"]["POS"]
        neg_prob = row["relation_probabilities"]["NEG"]
        comb_prob = pos_prob + neg_prob + row["relation_probabilities"]["COMB"]
        no_comb_prob = row["relation_probabilities"]["NO_COMB"]
        if pos_prob > args.label_threshold:
            relation_labels["POS"][drug_relation] += 1
        if neg_prob > args.label_threshold:
            relation_labels["NEG"][drug_relation] += 1
        if comb_prob > args.label_threshold:
            relation_labels["COMB"][drug_relation] += 1
        if no_comb_prob > args.label_threshold:
            relation_labels["NO_COMB"][drug_relation] += 1
    
    positive_relations = return_relations_meeting_frequency(relation_labels["POS"], args.min_frequency)
    negative_relations = return_relations_meeting_frequency(relation_labels["NEG"], args.min_frequency)
    no_comb_relations = return_relations_meeting_frequency(relation_labels["NO_COMB"], args.min_frequency*10)

    breakpoint()

    with open("positive_relations_20_thresh.json", 'w') as outfile:
        positives_writer = jsonlines.Writer(outfile)
        positives_writer.write_all(positive_relations)
    with open("negative_relations_20_thresh.json", 'w') as outfile:
        negatives_writer = jsonlines.Writer(outfile)
        negatives_writer.write_all(negative_relations)
    
